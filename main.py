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
function iotAction(robo){
    var requestURL = DEVICE_URL + "/?robo="+action
    $.get (requestURL)
    console.log(requestURL)
}
</script>
</head>
<center>
<div id="container">
<table cellpadding="0" cellspacing="0">
<tr>
<td style="padding-left:130px;" colspan="3">
<button style="width:440px;height:150px" ontouchstart="iotAction('forward')" ontouchend="iotAction('stop')"/>
</td>
</tr>
</table>
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
        client_sock=cl
        if not micropython_optimize:
            client_stream = client_sock.makefile("rwb")
        else:
            client_stream = client_sock
        req = client_stream.readline()
        get = req.split()[1].decode('utf-8')
        if get == '/?robo=forward':
            Robo.Forwrad()
            print("FORWARD")
        elif get == '/?robo=stop':
            Robo.Stop()
            print("Stop")
        elif get == '/?robo=backward':
            Robo.Backward()
            print("Backward")
        elif get == '/?robo=Left':
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