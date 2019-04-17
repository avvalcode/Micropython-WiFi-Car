import socket , machine
from AC_Robot import Robo

Robo = Robo(machine)

# html = """
# <!DOCTYPE html>
# <html>
#     <head> <title>ESP8266 Borad</title> </head>
#     <body> <h1>Hello From Wemos D1 Board</h1>
#     </body>
# </html>
# """
html = b"""
<html>
<head>
<script type="text/javascript">
var DEVICE_URL = 'http://'
function Action(robo){
    var requestURL = DEVICE_URL + "/?robo="+robo
    $.get (requestURL)
    }
</script>
<style>
        .button {
          background-color:white;
          border: 2px solid #555555;
          color:black;
          padding: 20px 32px;
          height: 100px;
          width: 200px;
          text-align: center;
          text-decoration: currentColor;
          display: inline-block;
          font-size: 32px;
          margin: 64px 32px;
          cursor: pointer;
          border-radius: 8px;
          grid-gap: 20px;
        }
</style>
</head>
<center>
<div id="container">
        <div class="col-md-1 btn-group">
            <button class="button" ontouchstart="Action('upleft')" ontouchend="Action('stop')">UpLeft</button>
            <button class="button" ontouchstart="Action('forward')" ontouchend="Action('stop')">Forward</button>
            <button class="button" ontouchstart="Action('upright')" ontouchend="Action('stop')">UpRight</button>
        </div>
        <div class="col-md-1 btn-group">
            <button class="button" ontouchstart="Action('left')" ontouchend="Action('stop')">Left</button>
            <button class="button" ontouchstart="Action('stop')" ontouchend="Action('stop')">Stop</button>
            <button class="button" ontouchstart="Action('right')" ontouchend="Action('stop')">Right</button>
        </div>
        <div class="col-md-1 btn-group">
            <button class="button" ontouchstart="Action('downleft')" ontouchend="Action('stop')">DownLeft</button>
            <button class="button" ontouchstart="Action('backward')" ontouchend="Action('stop')">Backward</button>
            <button class="button" ontouchstart="Action('downright')" ontouchend="Action('stop')">DownRight</button>
        </div>
</div>
</center>
</html>
"""

def Main(Robo):
    ip = '0.0.0.0'
    port = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip , port))
    # addr = socket.getaddrinfo('0.0.0.0' , 80)[0][-1]
    # s = socket.socket()
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.bind(addr)
    s.listen(5)

    while True:
        micropython_optimize = False
        cl , addr = s.accept()
        print("Connected from " , addr)
        if not micropython_optimize:
            client_stream = cl.makefile("rwb")
        else:
            client_stream = cl
        req = client_stream.readline()
        get = req.split()[1].decode('utf-8')
        print(get)
        if get == '/?robo=forward':
            Robo.Forwrad()
            print("FORWARD")
        elif get == '/?robo=stop':
            Robo.Stop()
            print("Stop")
        elif get == '/?robo=backward':
            Robo.Backward()
            print("Backward")
        elif get == '/?robo=left':
            Robo.Left()
            print("Left")
        elif get == '/?robo=right':
            Robo.Right()
            print("Right")
        elif get == '/?robo=upleft':
            Robo.Upleft()
            print("UpLeft")
        elif get == '/?robo=upright':
            Robo.Upright()
            print("UpRight")
        elif get == '/?robo=downleft':
            Robo.Downright()
            print("DownRight")
        elif get == '/?robo=downleft':
            Robo.Downleft()
            print("DownLeft")
        client_stream.write(html)
        client_stream.close()

Main(Robo)