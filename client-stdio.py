import asyncio
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

nest_asyncio.apply()  # Needed to run interactive python


async def main():
    # Define server parameters
    server_params = StdioServerParameters(
        command="python",  # The command to run your server
        args=["server.py"],  # Arguments to the command
    )

    # Connect to the server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tool_list = []
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")
                tool_list.append(tool.name)

            # choose tool
            while True:
                user_tool = str(input("\nEnter the tool you want to use: "))
                if user_tool in tool_list:
                    # Call our calculator tool
                    a = int(input("\nEnter 1st Number: "))
                    b = int(input("Enter 2nd Number: "))
                    result = await session.call_tool(
                        f"{user_tool}", arguments={"a": a, "b": b}
                    )
                    print(
                        f"\nResult:: {a} {result.content[1].text} {b} = {result.content[0].text}"
                    )
                    break
                else:
                    raise ValueError("Unknown tool:", user_tool)


if __name__ == "__main__":
    asyncio.run(main())
