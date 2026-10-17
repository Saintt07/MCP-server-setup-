module.exports = {
  apps: [
    {
      name: "mcp-server",
      script: "cmd.exe",
      args: "/c start.bat",
      max_restarts: 3, 
      autorestart: true
    },
    {
      name: "ngrok-tunnel",
      script: "ngrok",
      args: "http 8000",
      max_restarts: 3,
      autorestart: true
    }
  ]
};