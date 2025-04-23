from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv(".env")

# Create Model Context Protocol (MCP) Server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for Server-Sent Events (SSE) transport (localhost)
    port="8050",  # only used for SSE transport (set this to any port)
)


# Add simple calculator
@mcp.tool()
def add(a: int, b: int):
    """Add 2 numbers"""
    return a + b


# Run the server
if __name__ == "__main__":
    transport = "sse"  # Standard Input/Output (stdio)
    if transport == "stdio":
        print("Running stdio Transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError("Unknown transport:", transport)
