# server.py
import asyncio
import websockets
import keyboard

async def handle_client(websocket):
  async for message in websocket:
    if message == "PUSH":
      keyboard.press("space")
      print("Push-to-talk activated")
    elif message == "RELEASE":
      keyboard.release("space")
      print("Push-to-talk deactivated")

async def main():
  async with websockets.serve(handle_client, "0.0.0.0", 8765):
    print("Server running on ws://0.0.0.0:8765")
    await asyncio.Future()

if __name__ == "__main__":
  asyncio.run(main())
