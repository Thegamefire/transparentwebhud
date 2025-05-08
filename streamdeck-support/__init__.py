import websockets, asyncio
from websockets import ServerConnection
import json


async def open_websocket():
    async def open_connection(ws:ServerConnection):
        async for message in ws:
            await on_message(message, ws)

    async with websockets.serve(open_connection, "localhost", 8765) as server:
        await server.serve_forever()

async def on_message(msg, connection):
    if not msg.startswith("[SD_WEBHUD]"):
        return

    msg = json.loads(msg.removeprefix("[SD_WEBHUD]"))
    args = msg['args']

    match msg['command']:
        case "get page names":
            page_names = ["TestPage"] #TODO implement functionality

            response = "[SD_WEBHUD]"+json.dumps({
                "type":"page names",
                "data":page_names
            })
            await connection.send(response)
            print(f"return page names")

        case "toggle HUD-element":
            if len(args)<1:
                return
            if args["state"] is None:
                args["state"]='toggle'
            print(f"toggling element {args['name']} to state {args['state']}")

        case "move to":
            if len(args)<3:
                return

            print(f'Moving element {args['name']} to {args['x']},{args['y']}')

        case 'move':
            if len(args) < 3:
                return

            print(f'Moving element {args['name']} with diffs {args['x_diff']},{args['y_diff']}')

        case 'opacity change':
            if len(args)<2:
                return

            print(f'Changing opacity of element {args['name']} with diff {args['opacity_diff']}')



if __name__=='__main__':
    asyncio.run(open_websocket())