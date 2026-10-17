from pathlib import Path
import os

class WorkspaceSandbox:
    def __init__(self, workspace_root: str):
        # Convert to an absolute path to establish a strict boundary
        self.root = Path(workspace_root).resolve()
        
        # Ensure the sandbox directory actually exists
        if not self.root.exists():
            self.root.mkdir(parents=True, exist_ok=True)

    def get_safe_path(self, requested_path: str) -> Path:
        """
        Resolves a requested path against the workspace root and 
        prevents directory traversal escapes.
        """
        # Combine the root with the requested path
        # .resolve() evaluates all symlinks and '../' components to an absolute path
        target_path = (self.root / requested_path).resolve()

        # Security Check: The resolved path MUST start with the sandbox root path
        if not target_path.is_relative_to(self.root):
            raise PermissionError(
                f"Access Denied: Path '{requested_path}' attempts to escape the sandbox."
            )
        
        return target_path