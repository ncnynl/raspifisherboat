# raspifisherboat
Internet enabled Raspberry Pi fishing boat

Boat software consists of three projects:
 - BOAT:  python program which handles steering, gps, camera and other stuff. That software is in this project.
 - WEB UI: Angular 2 based web client Software for this is in separate project: https://github.com/ilkkaparssinen/...
 - SERVER: node.js server gets boat information via websockets and passess them forward to clients. Websocket connection is used also to pass information from client to boat (steering & speed). node.js is in separate project https://github.com/ilkkaparssinen/...

Boat features:
 - Two DC motors. Steering is done by adjusting the speed of the two motors (one on the right side and one on the left side). Controlling the motors is based on Adafruit Motor Hat and the libraries for that.
 - Internet connection (4G modem)
 - On board camera which transmits very low res MJPEG (6 frames/second ) via web sockets. Also on spearate command it takes full photos and sends them. This is based on the Raspberyy PI camera module and it's python libraries.
 - GPS location (location, speed and direction) is sent to the web server and there to clients, which show this information with google maps.
 - Option for adding a flex control to detect fish catches. (We didn't use this - too many wires..., but the code is there).
 - Option for playing music. We had a plan for "scientific" program to test if some sounds atrract fishes. Program switches between two mp3 files + some amount of silence.
 - Different speed variation programs for different kind of fishing.
 - Python 2.7 client. These raspberry tests are the first time I have programmed with python (but I like it) so the solution might not be very pythonesque, but in general the solution is quite clean. 

Web client features:
 - Speed and direction control of the boat
 - Multiple simultanous drivers (server acts as a publish & subscribe server, so everybody is in sync)
 - Real time video
 - Click the video screen and request for full res photo from boat
 - Set up different fishing programs / turn music on / off
 - Real time chat with other drivers and show notifications from the boat
 - Google maps - show location, direction and speed of the boat
 - Implemented with Angular 2 beta (things have changed in Angular 2 since that, and this was a learning project for me for Angular 2 - the software is ..uh.. not very good).
 
 Server features:
 - Web socket connection from the boat and to the clients. 
 - Simple pub/sub server
 - Can support multiple boats (each boat must have their own boat id)
 - Simple node.js websocket solution. This was a quick hack, but surpprisingly robust - I just put it running to EC2 and it just keeps running and responsing whenever we test the boat.
 
 
 
