import websockets
import asyncio

clients = {}


async def broadcast(username, message):
    for client in clients:
        await client.send(f"{username}: {message}")


async def handler(websocket):
    username = await websocket.recv()
    clients[websocket] = username
    print(f"{username} joined the chat!")

    try:
        async for message in websocket:
            print(f"{username}: {message}")
            await broadcast(username, message)
    finally:
        del clients[websocket]
        print(f"{username} left the chat!")


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server started...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
