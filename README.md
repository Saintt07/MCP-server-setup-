# 🔌 Custom Python FastMCP Server with Cline & ngrok

A lightweight, extensible Model Context Protocol (MCP) server built with Python (`FastMCP`), exposed securely to the internet via `ngrok`, managed by `PM2`, and integrated seamlessly with the `Cline` VS Code extension.

---

## What the Project Does

This project acts as a bridge between local Python scripts and AI assistants. It provisions a custom Model Context Protocol (MCP) server using Python's `FastMCP` framework, allowing AI clients like **Cline** to execute local workspace and system tools securely across an HTTP transport layer. 

Whether you're automating file operations, running data queries, or building custom agent workflows, this architecture provides a standardized interface for AI-driven execution.

---

## Why the Project Is Useful

* **Seamless AI Integration:** Instantly extends your VS Code AI assistant (`Cline`) with custom, locally-defined Python tools.
* **Secure Remote Tunneling:** Exposes your local server safely to the web using an `ngrok` tunnel, enabling cross-network AI tool execution.
* **Reliable Process Management:** Includes a pre-configured `PM2` ecosystem setup (`ecosystem.config.js`) for running and monitoring your background server processes smoothly.
* **Modular Design:** Clean separation of concerns between core server routing (`server.py`), tool definitions (`tools.py`), and configuration management (`config.py`).

---

## Project Structure

```text
my-mcp-project/
├── .env.example          # Template for required environment variables
├── .gitignore            # Excludes local logs, cache, and secrets
├── ecosystem.config.js   # PM2 background process configuration
├── server.py             # Main FastMCP server bootstrap script
├── tools.py              # Custom registered tools module
├── config.py             # Configuration loader
├── README.md             # Project documentation and guide
└── demo_transcript.md    # Recorded tool-call demo transcript & test run


Clone the repository:

Bash
git clone [https://github.com/Saintt07/MCP-server-setup-.git](https://github.com/Saintt07/MCP-server-setup-.git)
cd MCP-server-setup-
