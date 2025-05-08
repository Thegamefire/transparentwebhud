import asyncio
import json
import websockets


class WebSocketManager:
    def __init__(self):
        self.__shutdown_signal = asyncio.Event()

    def open_websocket(self):
        async def __start_ws():
            async with websockets.serve(
                    self.__on_connection,
                    "localhost",
                    8765
            ) as server:
                print("WebSocket Running")

                await self.__shutdown_signal.wait()
                server.close(close_connections=True)
                await server.wait_closed()

        asyncio.run(__start_ws())

    def close_websocket(self):
        self.__shutdown_signal.set()

    async def __on_connection(self, ws:websockets.ServerConnection):
        async for message in ws:
            if self.__shutdown_signal.is_set():
                await ws.close()
                return
            await self.__on_message(message, ws)

    async def __on_message(self, msg, connection):
        if not msg.startswith("[SD_WEBHUD]"):
            return

        msg = json.loads(msg.removeprefix("[SD_WEBHUD]"))
        args = msg['args']

        match msg['command']:
            case "get page names":
                page_names = ["TestPage"]  # TODO implement functionality

                response = "[SD_WEBHUD]" + json.dumps({
                    "type": "page names",
                    "data": page_names
                })
                await connection.send(response)
                print(f"return page names")

            case "toggle HUD-element":
                if len(args) < 1:
                    return
                if args["state"] is None:
                    args["state"] = 'toggle'
                print(f"toggling element {args['name']} to state {args['state']}")

            case "move to":
                if len(args) < 3:
                    return

                print(f'Moving element {args['name']} to {args['x']},{args['y']}')

            case 'move':
                if len(args) < 3:
                    return

                print(f'Moving element {args['name']} with diffs {args['x_diff']},{args['y_diff']}')

            case 'opacity change':
                if len(args) < 2:
                    return

                print(f'Changing opacity of element {args['name']} with diff {args['opacity_diff']}')


if __name__=='__main__':
    manager = WebSocketManager()
    manager.open_websocket()
    manager.close_websocket()