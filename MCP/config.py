import os
from pathlib import Path

WORKSPACE_ROOT = Path(os.getenv("WORKSPACE_ROOT", "./workspace")).resolve()
WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)

TUNNEL_USERNAME = os.getenv("MCP_USERNAME", "mcp_user")
TUNNEL_PASSWORD = os.getenv("MCP_PASSWORD", "secure_token")