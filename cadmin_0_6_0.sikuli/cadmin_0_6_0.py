import time;
import os;

Settings.OcrTextSearch = True

###### define variables and patterns used ######
networks = ['cadmin', '1234', 'net work name', '!#%.,_']
devices = ['online', 'offline', 'device']
status = ({ 'ON': 1, 'OFF': 0 })
devices_to_delete = ['online', 'device']


### visual dictionary ###
app = ({"cadmin": "imgs\\1435695722164.png" })
menubar = ({ "edit": "imgs\\1435753911188.png" })
toolbar = ({ "offline": "imgs\\1443959400381.png"
    , "online": "imgs\\1444146003908.png" })
actions = ({ "networks": "imgs\\1443526604930.png"
    , "add_device": "imgs\\1435757222352.png"
    , "manage_networks": "imgs\\1444134363912.png" })
menu_open = ({ "edit": "imgs\\1443517775071.png"})
buttons = ({ "n_new_name_ok": "imgs\\1443612344043.png"
    , "n_add": "imgs\\1435688561633.png"
    , "n_add_ok": "imgs\\1435700914588.png"
    , "d_add_ok": "imgs\\1435756929018.png" })
dialogs = ({ "main": "imgs\\1443522369700.png"
    , "network": "imgs\\1435688533049.png"
    , "n_new_name": "imgs\\1435689848501.png"
    , "add_device": "imgs\\1435776135971.png"
    , "manage_devices": Pattern("imgs\\1444134446816.png").similar(0.50)})
dev_type = ({ "farist3": "imgs\\1435756869777.png"
    , "farist4": "imgs\\1443691985751.png"
    , "combo": "imgs\\1443692271269.png"
    , "combo_farist3": "imgs\\1443692478591.png" })
dev_property = ({ "cert_cn": "imgs\\1444135626140.png" })
arrows = ({"left": "imgs\\1444138387854.png" })
buttons_manageDevs = ({ "add_delete": "imgs\\1444138663093.png"
    , "delete": "imgs\\1444138696257.png"
    , "ok_cancel": "imgs\\1444144799590.png"})
# dialog_manageDev = ({ })

# "1444221751858.png"

###### active app ######
def appActive(app):
    #self.app = app
    searchResult = App.focus(app)
    print("searchResult: " + str(searchResult))
    if (app in str(searchResult)):
        return 'True'
    else:
        return 'False'

###### add network ######
def addNetwork():
    print "--Add network--"
    find(menubar["edit"]).click(menubar["edit"])
    find(menu_open["edit"]).find(actions["networks"]).click(actions["networks"])
    i = 0
    while exists(dialogs["network"]) and i < len(networks):
        for network in networks:
            click(buttons["n_add"])
            type(dialogs["n_new_name"], network)
            wait(0.5)
            find(dialogs["n_new_name"]).find(buttons["n_new_name_ok"]).click(buttons["n_new_name_ok"])
            i = i+1
    find(buttons["n_add_ok"]).click(buttons["n_add_ok"])

###### add device ######
def addDevice():
    print "--add device--"
    i = 0
    while exists(menubar["edit"]) and i < len(devices):
        for device in devices:
            find(menubar["edit"]).click(menubar["edit"])
            find(menu_open["edit"]).find(actions["add_device"]).click(actions["add_device"])
            type(dialogs["add_device"], device)
            wait(0.5)
            if not find(dev_type["farist3"]):
                find(dev_type["farist4"]).click(dev_type["farist4"]).find(dev_type["combo"]).click(dev_type["combo_farist3"])
            else: 
                click(dev_type["farist3"])
                click(dev_type["farist3"])
            i = i+1
            find(buttons["d_add_ok"]).click(buttons["d_add_ok"])
			
###### delete device ######
def deleteDevice():
    print "--remove device--"
    find(menubar["edit"]).click(menubar["edit"])
    find(menu_open["edit"]).find(actions["manage_networks"]).click(actions["manage_networks"])
    i = 0
    t = 0
    manageDevs = dialogs["manage_devices"]
    wait(manageDevs)
    while exists(manageDevs) and i < len(devices) and t < len(devices):
        manageDevs = find(manageDevs).highlight(2)
        with Region(manageDevs):
            below_cert_cn = find(dev_property["cert_cn"]).below()
            below_cert_cn.highlight(2)
            # move device from network-side to available devices-side
            with Region(below_cert_cn):
                for device in devices:
                    if not exists(device):
                        print("\n---Device: " + str(device) + ", not found\n")
                    elif exists(device):
                        d = 0
                        for dev in findAll(device):
                            click(dev)
                            Region(manageDevs).find(arrows["left"]).click(arrows["left"])
                            print("\n---device moved: " + device + "\n")
                            d = d+1
                    i = i+1
            # delete device from available devices-side
            below_available_devs = find("Available devices").below().highlight(2)
            with Region(below_available_devs):
                for device in devices:
                    if not exists(device):
                        print("Device: " + str(device) + ", not found\n")
                    elif exists(device):
                        d = 0
                        for dev in findAll(device):
                            click(dev)
                            Settings.OcrTextSearch = True
                            Region(manageDevs).find(buttons_manageDevs["add_delete"]).find(buttons_manageDevs["delete"]).click(buttons_manageDevs["delete"])
                            print("device deleted: " + device + "\n")
                            d = d+1
                    t = t+1                
    ok_cancel = manageDevs.find(buttons_manageDevs["ok_cancel"]).highlight(2)
    print(\n1\n)
    with Region(ok_cancel):
        for x in Region(ok_cancel).findAll("OK"):
            print(\n2\n)
            print("x: " + str(x))
            Region(x).highlight(2)
            print(\n3\n)
            click(x)
    print "\n---done with region dialogs[manage_devices]---\n"
        
###### toggle online/offline status ######
def toggleStatus(status):
    if exists(dialogs["main"]):
        if (status == 'ON') and exists(toolbar["offline"]):
            click(toolbar["offline"])
            print("\n---status: " + status)
        elif (status == 'OFF') and exists(toolbar["online"]):
            click(toolbar["online"])
            print("\n---status: " + status)
	elif not exists(dialogs["main"]):
		switchApp(cadmin)
		# print("\n---switchApp testing")

###### begin test sequence ######
def initTestSequence():
    addNetwork()
    addDevice()
    toggleStatus('ON')
    deleteDevice()
        
###### script start ######
print ("\ncadmin_test.sikuli script running\n")
cadmin = App("C:\\Program Files (x86)\\Tutus\\CAdmin\\cadmin.exe")
cadmin = cadmin.open()
# wait(app["cadmin"])
if exists(app["cadmin"]) and not exists(dialogs["main"]):
	find(app["cadmin"]).click(app["cadmin"])	
	onAppear(dialogs["main"], initTestSequence())
elif exists(dialogs["main"]):
    initTestSequence()
else:
    print("\nCould not find CAdmin application\n")
	
print("---script done!")
cadmin.close()
# App.close(cadmin)

# during runtime, at every run, this script auto captures an image of the regions searched
# deleting these images to free up space (optional)
print("\n---deleting auto-captured images by script---\n")
imgPath = list(getImagePath())
for path in imgPath:
    print "path: ", path
    for file in os.listdir(path):
        if file.endswith(".png"):
            print "file: ", file, " will be deleted!"
            os.remove(path+file)
        else:
            print "no *.png files could be found\n"