🔌 Custom FastMCP Server with Cline & ngrok

A lightweight, extensible Model Context Protocol (MCP) server built with Python and FastMCP, exposed to the internet through ngrok, managed by PM2, and integrated with the Cline VS Code extension.

📌 Overview

This project bridges local Python scripts and AI assistants through a custom Model Context Protocol (MCP) server.

Built with Python's FastMCP framework, it allows AI clients such as Cline to interact with custom Python tools over an HTTP transport layer.

Whether you're automating file operations, running data queries, or building custom AI agent workflows, this project provides a foundation for extending AI assistants with your own tools.

✨ Features
🤖 AI Integration: Extend your Cline AI assistant with custom Python tools directly from VS Code.
🌐 Secure Remote Tunneling: Expose your local MCP server through an ngrok HTTPS tunnel.
⚙️ Process Management: Use PM2 to run, monitor, and manage background services.
🧩 Modular Architecture: Keep server initialization, tool definitions, and configuration organized in separate Python modules.
🔧 Extensible Tools: Add custom Python functions and expose them to compatible MCP clients.
🚀 Flexible Execution: Run the server manually during development or manage it with PM2.
🏗️ Project Structure
MCP-server-setup-/
├── .env.example          # Template for environment variables
├── .gitignore            # Excludes secrets, logs, and cache files
├── ecosystem.config.js   # PM2 process configuration
├── server.py             # FastMCP server entry point
├── tools.py              # Custom MCP tool definitions
├── config.py             # Configuration loader
├── README.md             # Project documentation
└── demo_transcript.md     # Example tool-call transcript

🛠️ Prerequisites

Before getting started, make sure you have the following installed:

Python 3.10 or higher
Node.js and npm
PM2 (can be run through npx)
ngrok with an active account
Visual Studio Code
Cline VS Code extension

You will also need an ngrok authentication token to establish your public tunnel.

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/Saintt07/MCP-server-setup-.git
cd MCP-server-setup-

2. Configure Environment Variables

Copy the example environment file:

cp .env.example .env


Open .env and configure the required environment variables.

Note: Never commit your .env file or expose API keys, authentication tokens, or other sensitive credentials in your repository.
3. Install Python Dependencies

Install the required Python packages:

pip install "m[cli]" fastmcp uvicorn pydantic


It is recommended to use a virtual environment to keep project dependencies isolated.

Create and activate a virtual environment:

python -m venv .venv


Windows:

.venv\Scripts\Activate.ps1


Linux/macOS:

source .ven
