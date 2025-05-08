import websockets, asyncio
from websockets import ServerConnection


async def open_websocket():
    async def open_connection(ws:ServerConnection):
        async for message in ws:
            await on_message(message)

    async with websockets.serve(open_connection, "localhost", 8765) as ws:
        await ws.serve_forever()

async def on_message(msg):
    if not msg.startswith("[SD_WEBHUD] "):
        return

    msg = msg.removeprefix("[SD_WEBHUD] ")
    args = msg.split(" ")
    command = args.pop(0)

    match command:
        case "toggle_HUD_element":
            if len(args)<1:
                return
            print(f"toggling element {args[0]}")

        case "move_to":
            if len(args)<3:
                return

            page_name = args[0]
            x = args[1]
            y = args[2]

            print(f'Moving element {page_name} to {x},{y}')

        case 'move_diff':
            if len(args) < 3:
                return

            page_name = args[0]
            x_diff = args[1]
            y_diff = args[2]

            print(f'Moving element {page_name} with diffs {x_diff},{y_diff}')

        case 'opacity_diff':
            if len(args)<2:
                return

            page_name = args[0]
            opacity_diff = args[1]
            print(f'Changing opacity of element {page_name} with diff {opacity_diff}')



if __name__=='__main__':
    asyncio.run(open_websocket())