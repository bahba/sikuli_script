import time;

###### define variables and patterns used ######
networks = ['cadmin', '1234', 'net work name', '!#%.,_']
devices = ['online', 'offline', 'device']


### visual dictionary ###
app = ({"cadmin": "1435695722164.png" })
menubar = ({ "edit": Pattern("1435753911188.png").similar(0.60) }) 
actions = ({ "networks": "1443526604930.png", "add_device": "1435757222352.png" })
menu_open = ({ "edit": "1443517775071.png"})
buttons = ({ "n_new_name_ok": "1443612344043.png", "n_add": "1435688561633.png", "n_add_ok": "1435700914588.png", "d_add_ok": "1435756929018.png" })
dialogs = ({ "main": "1443522369700.png", "network": "1435688533049.png", "n_new_name": "1435689848501.png", "add_device": "1435776135971.png"})
dev_type = ({ "farist3": "1435756869777.png", "farist4": "1443691985751.png", "combo": "1443692271269.png", "combo_farist3": "1443692478591.png" })


###### add network ######
def addNetwork():
    print "--Add network--"
    click(menubar["edit"])
    find(menu_open["edit"]).find(actions["networks"]).click(actions["networks"])
    i = 0
    while exists(dialogs["network"]) and i < len(networks):
        print "i: ", i 
        print "len(networks): ", len(networks)
        for network in networks:
            print "network: ", network
            print "i: " , i
            click(buttons["n_add"])
            type(dialogs["n_new_name"], network)
            wait(1)
            find(dialogs["n_new_name"]).find(buttons["n_new_name_ok"]).click(buttons["n_new_name_ok"])
            i = i+1
            print "i: ", i            
    click(buttons["n_add_ok"])

###### add device ######
def addDevice():
    print "--add device--"
#    click(menubar["edit"])
#    find(menu_open["edit"]).find(actions["add_device"]).click(actions["add_device"])
    i = 0
    while exists(menubar["edit"]) and i < len(devices):
        #dialogs["add_device"]
        click(menubar["edit"])
        find(menu_open["edit"]).find(actions["add_device"]).click(actions["add_device"])
        print "i: ", i    
        print "len(devices): ", len(devices)
        for device in devices:
            print "device: ", device
            print "i: ", i
            type(device)
            wait(1)
            if not find(dev_type["farist3"]):
                find(dev_type["farist4"]).click(dev_type["farist4"]).find(dev_type["combo"]).click(dev_type["combo_farist3"])
            else: 
                click(dev_type["farist3"])
                click(dev_type["farist3"])
            i = i+1        
            print "i: ", i
            click(buttons["d_add_ok"])
            break
#            Region(dialogs["add_device"]).inside().find(dialogs["add_device"]).click(buttons["d_add_ok"])
#    "1435694432835.png"


###### script start ######
print ("cadmin_test.sikuli script running")
cadmin = App("C:\\Program Files (x86)\\Tutus\\CAdmin\\cadmin.exe")
#cadmin = App.open("C:\\Program Files (x86)\\Tutus\\CAdmin\\cadmin.exe")
if not cadmin.window():
    cadmin.open()
wait(5)
cadmin.focus()
with Region(cadmin.window()):
    #onAppear(cadmin.window(), addNetwork())
    addNetwork()
    #onAppear(dialogs["main"], addDevice())
    addDevice()
cadmin.close()

