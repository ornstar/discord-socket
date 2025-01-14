# client.py
import asyncio
import websockets
import keyboard

server_url = "ws://localhost:8765"
key_to_monitor = "space"

async def send_key_events():
  async with websockets.connect(server_url) as websocket:
    print(f"Connected to server at {server_url}")
    is_pressed = False

    while True:
      try:
        if keyboard.is_pressed(key_to_monitor) and not is_pressed:
          await websocket.send("PUSH")
          print("Sent PUSH")
          is_pressed = True
        elif not keyboard.is_pressed(key_to_monitor) and is_pressed:
          await websocket.send("RELEASE")
          print("Sent RELEASE")
          is_pressed = False
        await asyncio.sleep(0.1)
      except Exception as e:
        print(f"Error: {e}")
        break

if __name__ == "__main__":
  asyncio.run(send_key_events())
