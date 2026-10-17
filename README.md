# FastMCP Server with Cline & ngrok

A lightweight, locally-hosted Python Model Context Protocol (MCP) server. This project seamlessly connects your local Python tools to the Cline VS Code extension securely across the internet using an ngrok tunnel.

## 🏆 Project Milestones & Features
* **Milestone 1: Custom MCP Server:** Fully operational Model Context Protocol server built with Python's `FastMCP`.
* **Milestone 2: Secure Remote Tunneling:** Local port 8000 safely exposed to the web via `ngrok` for external AI client access.
* **Milestone 3: Background Management:** Daemonized process execution using `PM2` (`ecosystem.config.js`) for persistent uptime.
* **Milestone 4: Cline Integration:** Seamless handshake with the VS Code Cline AI extension to execute local scripts autonomously.

## 🧰 Included MCP Tools
The server currently provides the AI with the following custom workspace and version-control tools (defined in `tools.py`):
* `read`: Reads the contents of specified files from the local filesystem.
* `list`: Lists files and directories within a specified path.
* `write`: Generates new files or overwrites existing ones with new code and content.
* `delete`: Safely removes unwanted files or folders from the workspace.
* `str_replace`: Performs targeted string replacements within an existing file.
* `search files`: Scans the workspace to locate specific file names or text patterns.
* `git_init`: Initializes a new, empty Git repository in the designated directory.
* `git_status`: Retrieves the current status of the Git working tree (staged, unstaged, and untracked files).

## 💻 Minimum Requirements
* **OS:** Windows / macOS / Linux
* **Environment:** Python 3.10+ and Node.js (with npm)
* **Editor:** VS Code with the **Cline** extension installed
* **Network:** An active [ngrok](https://ngrok.com/) account and authentication token
