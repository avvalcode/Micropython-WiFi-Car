import esp
import gc

def Connection():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    try:
        print("connecting ...")
        sta_if.connect('YOUR_SSID', 'YOUR_WIFI_PASS')
        print("connected to ", sta_if.ifconfig()[0])
    except:
        sta_if.isconnected() == True

Connection()
gc.collect()
