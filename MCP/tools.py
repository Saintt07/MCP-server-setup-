import os
import subprocess
from pathlib import Path
from config import WORKSPACE_ROOT

class WorkspaceSandbox:
    def __init__(self, workspace_root: Path):
        self.root = workspace_root.resolve()
        if not self.root.exists():
            self.root.mkdir(parents=True, exist_ok=True)

    def get_safe_path(self, requested_path: str) -> Path:
        """
        Resolves a requested path against the workspace root and 
        rejects escapes to enforce the sandboxed workspace requirement[cite: 1].
        """
        target_path = (self.root / requested_path).resolve()
        if not target_path.is_relative_to(self.root):
            raise PermissionError(f"Access Denied: Path '{requested_path}' attempts to escape the sandbox.")
        return target_path

# Initialize the sandbox using the configuration root
sandbox = WorkspaceSandbox(WORKSPACE_ROOT)

def register_tools(mcp):
    
    @mcp.tool()
    def list_files() -> str:
        """List all files in the sandboxed workspace directory."""
        # Using rglog to recursively list files inside the sandbox
        files = [str(p.relative_to(sandbox.root)) for p in sandbox.root.rglob('*') if p.is_file()]
        return f"Files: {', '.join(files)}" if files else "Workspace is empty."

    @mcp.tool()
    def read_file(path: str) -> str:
        """Read the contents of a file inside the workspace."""
        try:
            safe_path = sandbox.get_safe_path(path)
            if not safe_path.exists():
                return "Error: File does not exist."
            return safe_path.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    def write_file(path: str, content: str) -> str:
        """Write new content to a file inside the workspace."""
        try:
            safe_path = sandbox.get_safe_path(path)
            safe_path.parent.mkdir(parents=True, exist_ok=True)
            safe_path.write_text(content, encoding="utf-8")
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    def delete_file(path: str) -> str:
        """Delete a file inside the workspace."""
        try:
            safe_path = sandbox.get_safe_path(path)
            if not safe_path.exists():
                return "Error: File does not exist."
            safe_path.unlink()
            return f"Successfully deleted {path}"
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    def str_replace(path: str, old_str: str, new_str: str) -> str:
        """Replace one exact occurrence of old_str in a file. Fails if the match is not unique[cite: 1]."""
        try:
            safe_path = sandbox.get_safe_path(path)
            if not safe_path.exists():
                return "Error: File does not exist."
            content = safe_path.read_text(encoding="utf-8")
            if content.count(old_str) != 1:
                return "Error: old_str must appear exactly once."
            safe_path.write_text(content.replace(old_str, new_str), encoding="utf-8")
            return f"Successfully replaced text in {path}"
        except Exception as e:
             return f"Error: {str(e)}"

    @mcp.tool()
    def search_files(query: str) -> str:
        """Search for a specific string across all text files in the workspace."""
        results = []
        for filepath in sandbox.root.rglob("*.*"):
            if filepath.is_file():
                try:
                    if query in filepath.read_text(errors='ignore'):
                        results.append(str(filepath.relative_to(sandbox.root)))
                except Exception:
                    continue
        return f"Found '{query}' in: {', '.join(results)}" if results else "No matches found."

    @mcp.tool()
    def git_init() -> str:
        """Initialize a git repository in the workspace to track state changes."""
        try:
            result = subprocess.run(["git", "init"], cwd=sandbox.root, capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    def git_status() -> str:
        """Check the git status of the workspace to see modified files."""
        try:
            result = subprocess.run(["git", "status", "-s"], cwd=sandbox.root, capture_output=True, text=True)
            return result.stdout or "Working tree clean."
        except Exception as e:
            return f"Error: {str(e)}"