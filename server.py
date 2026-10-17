from fastmcp import FastMCP
from tools import register_tools
import config

mcp = FastMCP("connector")

register_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport = "http", 
            port = 8000)