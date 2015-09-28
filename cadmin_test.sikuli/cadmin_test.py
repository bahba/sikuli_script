import time;

networks = ['cadmin', '1234', 'net work name', '!#%.,_']
devices = ['online', 'offline', 'device']

###### open App ######
print "--open app--"
myApp = App("cadmin")
#if App.open(myApp):
#    print "im up"

reg = Region(Screen.getBounds(Screen(0)))
print "reg.getTopLeft(): ", reg.getTopLeft()

#pattern().similar.(0.8).anyColor().anySize()
if not exists("1435695722164.png"):
    App.open("C:\\Program Files (x86)\\Tutus\\CAdmin\\cadmin.exe")
    wait(1)
    myApp.focus()
    splashScreen = App.focusedWindow()
    time.sleep(3)
    myApp = App.focusedWindow()
    wait(1)
    print "myApp: ", myApp
else:
    print "else"
    find("1435695722164.png").highlight(1)
    click("1435695722164.png")
    wait(1)
    print "clicked"
#if find("1435753753369.png"):
#print "not exists login page"
#click("1435695722164.png")        
wait(1)

###### add network ######
print "--Add network--"
click("1435753911188.png")
type (Key.DOWN)
type (Key.ENTER)

i = 0
while exists("1435688533049.png") and i < len(networks):
    print "i: ", i 
    print "len(networks): ", len(networks)
    for network in networks:
        print "network: ", network
        print "i: " , i
        click("1435688561633.png")
        type("1435689848501.png", network)   
        wait(1)
        click("1435700914588.png")
        i = i+1
        print "i: ", i
click("1435784806314.png")

###### add device ######
print "--add device--"
wait(1)
click("1435753911188-1.png")
type(Key.DOWN)
type(Key.DOWN)
type(Key.ENTER)
#click("1435757222352.png")

i = 0
while exists("1435776135971.png") and i < len(devices):
    print "i: ", i    
    print "len(devices): ", len(devices)
    for device in devices:
        print "device: ", device
        print "i: ", i
        type(device)
        wait(1)
        click("1435756869777.png")
        type(Key.DOWN)
        type(Key.ENTER)
        click("1435756929018.png")
        i = i+1        
        print "i: ", i

#    "1435694432835.png"
