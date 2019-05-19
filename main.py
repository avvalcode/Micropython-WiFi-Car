import machine 
from AC_Robot import Robo

try:
    import usocket as socket
except:
    import socket

Robo = Robo(machine)

html = b"""<!DOCTYPE html>
<html>
<head>
<script type="text/javascript">
function ajax(url) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", url);
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if(xmlhttp.status == 200){
                console.log('Response: ' + xmlhttp.responseText );
            }else{
                console.log('Error: ' + xmlhttp.statusText )
            }
        }
    }
    xmlhttp.send(null);
}
var DEVICE_URL = ''
function Action(robo){
    var requestURL = DEVICE_URL + "/?robo="+robo
    ajax(requestURL)
}
</script>
<style>
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        height: 100vh;
        margin: 0;
    }
    a {
        text-decoration: none;
        color: #333;
    }
    h2, p {
        margin: 0;
        padding: 0;
    }
    #header {
        text-align: center;
        padding: 15px 0;
        background: #f8f8f8;
        width: 100%;
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.3);
        height: 80px;
        box-sizing: border-box;
    }
    #container {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #footer {
        font-family: monospace;
        font-size: 10px;
    }
    .row {
        display: flex;
        flex: 1;
    }
    .row .col {
        flex: 1;
        width: 33vw;
        height: 33vw;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .row .col button {
        width: 90%;
        height: 90%;
        border-radius: 99em;
        border: none;
        background: #fff;
    }
</style>
</head>
<div id="header">
    <a href="https://avvalcode.com">
        <h2>AvvalCode WiFi Robot</h2>
        <p>Micropython on ESP8266</p>
    </a>
</div>
<div id="container">
    <div class="controller">
        <div class="row">
            <div class="col">
                <button ontouchstart="Action('upleft')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M41.36539,127.00962c-7.38462,-36.92308 -4.44231,-80.48077 -3.69231,-81.95192c0,-1.5 0.72115,-3.69231 2.19231,-4.44231c1.5,-1.47116 2.97115,-2.9423 4.4423,-2.9423c1.47116,0 45.0577,-2.97116 81.98077,3.69231c2.9423,0.72115 5.16346,2.9423 5.88462,5.16346c0.75,2.94231 0,5.91347 -2.19231,8.10577l-19.21154,19.96154c0,0 43.5577,48.72115 44.30769,52.41346c0.75,5.16346 -3.69231,14.04808 -9.60577,19.21153c-5.91346,5.91347 -13.29808,9.60577 -18.46154,8.85577c-3.69231,-0.75 -53.16346,-43.55769 -53.16346,-43.55769l-19.21153,19.18269c-2.19231,2.22115 -5.16346,2.97116 -7.38462,2.22115c-2.94231,-0.75 -5.16346,-2.9423 -5.88462,-5.91346z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('forward')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M36.92308,83.45192c20.68269,-31.00961 53.16346,-59.07692 54.63462,-59.82692c0.75,-0.72115 2.97115,-1.47116 4.4423,-1.47116c1.47116,0 3.69231,0.75 5.16346,1.47116c1.47116,0.75 33.98077,29.53846 54.66346,59.82692c1.47115,2.22116 1.47115,5.16346 0.72115,8.10577c-1.47116,2.22115 -3.69231,4.4423 -6.63462,4.4423h-27.3173c0,0 -3.69231,64.24039 -5.91347,67.21154c-3.69231,3.69231 -12.54807,6.63461 -20.68269,6.63461c-8.13461,0 -16.24039,-2.9423 -19.21153,-6.63461c-1.47116,-2.97116 -6.63462,-67.21154 -6.63462,-67.21154h-27.31731c-2.97115,0 -5.16346,-1.47116 -6.66346,-4.4423c-1.47116,-2.19231 -0.72116,-5.16346 0.75,-8.10577z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('upright')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M64.99038,41.36539c36.92308,-7.38462 80.48077,-4.44231 81.95193,-3.69231c1.5,0 3.69231,0.72115 4.4423,2.19231c1.47116,1.5 2.22115,2.97115 2.22115,4.4423c0,1.47116 2.94231,45.0577 -3.69231,81.98077c-0.75,2.9423 -2.97115,5.16346 -5.16346,5.88462c-2.97116,0.75 -5.91347,0 -8.13462,-2.19231l-19.21153,-19.21154c0,0 -48.72116,43.5577 -52.41347,44.30769c-5.16346,0.75 -14.04807,-3.69231 -19.21153,-9.60577c-5.91346,-5.16346 -9.60577,-13.29808 -8.85577,-18.46154c0.75,-3.69231 43.5577,-53.16346 43.5577,-53.16346l-19.1827,-19.21153c-2.22115,-2.19231 -2.97115,-5.16346 -2.22115,-7.38462c0.75,-2.94231 2.94231,-5.16346 5.91346,-5.88462z"></path>
                    </svg>
                </button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <button ontouchstart="Action('left')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M83.45192,155.07692c-31.00961,-20.68269 -59.07692,-53.16346 -59.82692,-54.63461c-0.72115,-0.75 -1.47116,-2.97116 -1.47116,-4.44231c0,-1.47116 0.75,-3.69231 1.47116,-5.16346c0.75,-1.47115 29.53846,-33.98077 59.82692,-54.66346c2.22116,-1.47116 5.16346,-1.47116 8.10577,-0.72116c2.97115,2.22116 4.4423,4.41347 4.4423,7.38462v27.31731c0,0 64.24039,3.69231 67.21154,5.91346c4.41346,2.94231 6.63461,12.54808 6.63461,19.93269c0,8.13462 -2.9423,16.24039 -6.63461,19.21154c-2.97116,2.19231 -67.21154,6.63461 -67.21154,6.63461v27.31731c0,2.97116 -1.47116,5.16346 -4.4423,6.66346c-2.19231,1.47115 -5.16346,0.72115 -8.10577,-0.75z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('stop')" ontouchend="Action('stop')">
                    <svg width="70%" viewBox="0 0 192 192">
                        <path d="M155.07692,147.69231c0,4.06731 -3.31731,7.38462 -7.38462,7.38462h-103.38462c-4.06731,0 -7.38462,-3.31731 -7.38462,-7.38462v-103.38462c0,-4.06731 3.31731,-7.38462 7.38462,-7.38462h103.38462c4.06731,0 7.38462,3.31731 7.38462,7.38462z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('right')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M108.54808,36.92308c31.00962,20.68269 59.07692,53.16346 59.82692,54.63462c1.47116,1.5 1.47116,2.97115 1.47116,5.19231c0,1.47115 -0.75,3.69231 -1.47116,5.16346c-0.75,1.47116 -29.53846,33.95193 -59.82692,54.63462c-2.22115,1.47116 -5.16346,1.47116 -8.10577,0.75c-2.22116,-1.47115 -4.44231,-3.69231 -4.44231,-6.66346v-27.31731c0,0 -64.24039,-3.69231 -67.21153,-5.91346c-3.69231,-4.41347 -6.63462,-13.26923 -6.63462,-21.40385c0,-8.13461 2.94231,-16.24039 6.63462,-19.21153c2.97115,-1.47116 67.21153,-6.63462 67.21153,-6.63462v-27.31731c0,-2.97115 1.47116,-5.16346 4.44231,-6.66346c2.19231,-1.47116 5.16346,-0.72116 8.10577,0.75z"></path>
                    </svg>
                </button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <button ontouchstart="Action('downleft')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M127.00962,150.63462c-36.92308,7.38462 -80.48077,4.4423 -81.95192,3.69231c-1.5,0 -3.69231,-0.72116 -4.44231,-2.19231c-1.47116,-1.5 -2.22115,-2.97116 -2.22115,-4.44231c0,-1.47116 -2.94231,-45.05769 3.69231,-81.98077c0,-2.94231 2.22115,-5.16346 5.16346,-5.88462c2.97115,-0.75 5.91346,0 8.13461,2.19231l19.21154,19.21153c0,0 48.72115,-43.55769 52.41346,-44.30769c5.16346,-0.75 14.04808,3.69231 19.21153,9.60577c5.91347,5.16346 9.60577,13.29808 8.85577,18.46154c-0.75,3.69231 -43.55769,53.16346 -43.55769,53.16346l19.18269,19.21154c2.22115,2.19231 2.97116,5.16346 2.22115,8.10577c-0.75,2.22115 -2.9423,4.4423 -5.91346,5.16346z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('backward')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M155.07692,108.54808c-20.68269,31.00962 -53.16346,59.07692 -54.63461,59.82692c-0.75,0.72116 -2.97116,1.47116 -4.44231,1.47116c-1.47116,0 -3.69231,-0.75 -5.16346,-1.47116c-1.47115,-0.75 -33.98077,-29.53846 -54.66346,-59.82692c-1.47116,-2.22115 -1.47116,-5.16346 -0.72116,-8.10577c2.22116,-2.97116 4.41347,-4.44231 7.38462,-4.44231h27.31731c0,0 3.69231,-64.24039 5.91346,-67.21153c2.94231,-3.69231 11.79808,-6.63462 19.93269,-6.63462c8.13462,0 16.24039,2.94231 19.21154,6.63462c2.19231,2.97115 6.63461,67.21153 6.63461,67.21153h27.31731c2.97116,0 5.16346,1.47116 6.66346,4.44231c1.47115,2.19231 0.72115,5.16346 -0.75,8.10577z"></path>
                    </svg>
                </button>
            </div>
            <div class="col">
                <button ontouchstart="Action('downright')" ontouchend="Action('stop')">
                    <svg viewBox="0 0 192 192">
                        <path d="M150.63462,64.99038c7.38462,36.92308 4.4423,80.48077 3.69231,81.95193c0,1.5 -0.72116,3.69231 -2.19231,4.4423c-1.5,0.75 -2.97116,2.22115 -4.44231,2.22115c-1.47116,0 -45.05769,2.94231 -81.98077,-3.69231c-2.94231,-0.75 -5.16346,-2.97115 -5.88462,-5.16346c-0.75,-2.97116 0,-5.91347 2.19231,-8.13462l19.21153,-19.21153c0,0 -43.55769,-48.72116 -44.30769,-52.41347c-0.75,-5.16346 3.69231,-13.29808 9.60577,-19.21153c5.16346,-5.91346 13.29808,-9.60577 18.46154,-8.85577c3.69231,0.75 53.16346,43.5577 53.16346,43.5577l19.21154,-19.1827c2.19231,-2.22115 5.16346,-2.97115 7.38462,-2.22115c2.9423,0.75 5.16346,2.94231 5.88462,5.91346z"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</div>
<div id="footer">
    MicroPython WiFi Controller v0.1
</div>
</html>
"""

def Main(Robo , micropython_optimize = False):
    # ip = '0.0.0.0'
    # ip = ''
    # port = 80
    s = socket.socket()
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind((ip , port))
    addr = socket.getaddrinfo('0.0.0.0' , 80)[0][-1]
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)

    while True:
        
        cl , addr = s.accept()
        print("Connected from " , addr)
        if not micropython_optimize:
            client_stream = cl.makefile("rwb")
        else:
            client_stream = cl
        req = client_stream.readline()
        # print(req)
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
        elif get == '/?robo=downright':
            Robo.Downright()
            print("DownRight")
        elif get == '/?robo=downleft':
            Robo.Downleft()
            print("DownLeft")
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            # print(h)
        client_stream.write(html)
        client_stream.close()
        if not micropython_optimize:
            cl.close()

Main(Robo)