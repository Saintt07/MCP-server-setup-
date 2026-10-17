Markdown
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
```
Getting Started
Prerequisites
Ensure you have the following installed on your local machine:

Python 3.10 or higher

Node.js & npm (required for pm2 and ngrok)

VS Code with the Cline extension installed

An active ngrok account with your local auth token configured

Installation & Setup
Clone the repository:
```
Bash
git clone [https://github.com/Saintt07/MCP-server-setup-.git](https://github.com/Saintt07/MCP-server-setup-.git)
cd MCP-server-setup-
```

Set up your environment variables:
Copy the example environment file and fill in your credentials:
```
Bash
cp .env.example .env
```

Install Python dependencies:
```
Bash
pip install "m[cli]" fastmcp uvicorn pydantic
```

Authenticate ngrok (First-time setup only):
```
Bash
ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
```

## Running the Server

Option A: Manual Run (Recommended for Development & Debugging)
Start your Python FastMCP server in your first terminal:
```
Bash
python server.py
```

In a separate terminal, launch your ngrok tunnel pointing to port 8000:
```
Bash
ngrok http 8000
```

Option B: Background Management (PM2)
To run your services silently in the background:
```
Bash
npx pm2 start ecosystem.config.js
```

Connecting to Cline
Copy your active public ngrok HTTPS URL (e.g., https://xxxx.ngrok-free.app).

Open your Cline MCP settings file (cline_mcp_settings.json) and configure your server endpoint with the required /mcp transport path:
```
JSON
{
  "mcpServers": {
    "connector": {
      "url": "[https://YOUR-NGROK-URL.ngrok-free.app/mcp](https://YOUR-NGROK-URL.ngrok-free.app/mcp)"
    }
  }
}
```
Reload your VS Code window (Ctrl+Shift+P -> Developer: Reload Window).

The green connected status and your custom Python tools will automatically populate in Cline! You can review demo_transcript.md for a sample execution log of a successful test run.

## Support & Help
If you encounter connection errors or need assistance with tool configuration:

Verify that your Python server terminal is actively running and listening on port 8000.

Confirm your ngrok tunnel is active and your public URL matches your cline_mcp_settings.json file.

Review the demo_transcript.md file for expected output behaviors.

Maintainers & Contributing
Maintained by Saintt07.

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request for improvements.
