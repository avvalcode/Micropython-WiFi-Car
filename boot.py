import esp
import gc

def Connection():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    try:
        print("connecting ...")
        sta_if.connect('Your_WIFI_ssid', 'Your_WIFI_pass')
        print("connected to ", sta_if.ifconfig()[0])
    except:
        sta_if.isconnected() == True

Connection()
gc.collect()
