import time;
import os;

Settings.OcrTextSearch = True
# Settings.MinSimilarity = 0.50

###### define variables and patterns used ######
networks = ['cadmin', '1234', 'net work name', '!#%.,_']
devices = ['online', 'offline', 'device']
status = ({ 'ON': 1, 'OFF': 0 })
devices_to_delete = ['online', 'device']
# certCNs = ({ 'd01': 'srv-d01.test.tutus.se', 'd02': 'srv-d02.test.tutus.se', 'test': 'test.test.tutus.se' })
certCNs = ['srv-d01.test.tutus.se', 'srv-d02.test.tutus.se', 'test.test.tutus.se']
# addresses = ({ 'd01': '10.17.0.110', 'd02': '10.17.0.113', 'moc': '127.0.0.1' })
addresses = ['10.17.0.110', '10.17.0.113', '127.0.0.1']
port = ['443']


### visual dictionary ###
# app = ({"cadmin": Pattern("imgs\\1435695722164.png").similar(0.50) })
# menubar = ({ "edit": Pattern("imgs\\1435753911188.png").similar(0.50)
    # , "window": Pattern("imgs\\1444390827151.png").similar(0.50) })
# toolbar = ({ "offline": Pattern("imgs\\1443959400381.png").similar(0.50)
    # , "online": Pattern("imgs\\1444146003908.png").similar(0.50) })
# actions = ({ "networks": Pattern("imgs\\1443526604930.png").similar(0.50)
    # , "add_device": Pattern("imgs\\1435757222352.png").similar(0.50)
    # , "manage_networks": Pattern("imgs\\1444134363912.png").similar(0.50) })
# menu_open = ({ "edit": Pattern("imgs\\1443517775071.png").similar(0.50)
    # , "window": Pattern("imgs\\1444390974327.png").similar(0.50)})
# buttons = ({ "n_new_name_ok": Pattern("imgs\\1443612344043.png").similar(0.50)
    # , "n_add": Pattern("imgs\\1435688561633.png").similar(0.50)
    # , "n_add_ok": Pattern("imgs\\1435700914588.png").similar(0.50)
    # , "d_add_ok": Pattern("imgs\\1435756929018.png").similar(0.50) })
# dialogs = ({ "main": Pattern("imgs\\1443522369700.png").similar(0.50)
    # , "network": Pattern("imgs\\1435688533049.png").similar(0.50)
    # , "n_new_name": Pattern("imgs\\1435689848501.png").similar(0.50)
    # , "add_device": Pattern("imgs\\1435776135971.png").similar(0.50)
    # , "manage_devices": Pattern("imgs\\1444134446816.png").similar(0.50)})
# dev_type = ({ "farist3": Pattern("imgs\\1435756869777.png").similar(0.50)
    # , "farist4": Pattern("imgs\\1443691985751.png").similar(0.50)
    # , "combo": Pattern("imgs\\1443692271269.png").similar(0.50)
    # , "combo_farist3": Pattern("imgs\\1443692478591.png").similar(0.50) })
# dev_property = ({ "cert_cn": Pattern("imgs\\1444135626140.png").similar(0.50) })
# arrows = ({"left": Pattern("imgs\\1444138387854.png").similar(0.50) })
# buttons_manageDevs = ({ "add_delete": Pattern("imgs\\1444138663093.png").similar(0.50)
    # , "delete": Pattern("imgs\\1444138696257.png").similar(0.50)
    # , "ok_cancel": Pattern("imgs\\1444144799590.png").similar(0.50)})

    # "1444469331160.png"
app = ({"cadmin": "imgs\\1444650872939.png" }) #"1444650872939.png"
menubar = ({ "edit": "imgs\\1435753911188.png"
    , "window": "imgs\\1444390827151.png"})
toolbar = ({ "tools": "imgs\\1444667646570.png"
    , "offline": "imgs\\1443959400381.png"
    , "online": "imgs\\1444146003908.png" 
    , "add_dev": "imgs\\1444653692615.png"
    , "del_dev": Pattern("imgs\\1444653720544.png").similar(0.90) })
actions = ({ "networks": "imgs\\1443526604930.png"
    , "add_device": "imgs\\1444638936494.png"
    , "manage_networks": "imgs\\1444134363912.png" })
    # , "window": "imgs\\1444390974327.png" })
menu_open = ({ "edit": "imgs\\1444638373851.png" 
    , "window": "imgs\\1444390974327.png" })
buttons = ({ "n_new_name_ok": "imgs\\1443612344043.png"
    , "n_add": "imgs\\1435688561633.png"
    , "n_add_ok": "imgs\\1435700914588.png"
    , "d_add_ok": "imgs\\1435756929018.png" })
dialogs = ({ "main": "imgs\\1444469331160.png"
    , "network": "imgs\\1435688533049.png"
    , "n_new_name": "imgs\\1435689848501.png"
    # , "add_device": "imgs\\1435776135971.png"
    , "add_device": "imgs\\1444639102078.png"
    , "manage_devices": Pattern("imgs\\1444134446816.png").similar(0.50)})
dev_type = ({ "farist3": "imgs\\1435756869777.png"
    , "farist4": "imgs\\1443691985751.png"
    , "combo": "imgs\\1443692271269.png"
    , "combo_farist3": "imgs\\1443692478591.png" })
dev_property = ({ "cert_cn": "imgs\\1444135626140.png"
    , "name": "imgs\\1444666775117.png" })
arrows = ({"left": "imgs\\1444138387854.png" })
buttons_manageDevs = ({ "add_delete": "imgs\\1444138663093.png"
    , "delete": "imgs\\1444138696257.png"
    , "ok_cancel": "imgs\\1444144799590.png" })
lineEdits = ({ "text_field": "imgs\\1444641956354.png"
    , "name": "imgs\\1444647727714.png"
    , "cert_cn": "imgs\\1444647961595.png"
    , "address": "imgs\\1444647997108.png"
    , "port": "imgs\\1444648076724.png" })
popups = ({ "del_dev_confirm": "imgs\\1444657938720.png","test": "imgs\\1444746032022.png"})
popups_buttons = ({ "yes_no": "imgs\\1444745398796.png"
    , "yes": "imgs\\1444745467019.png"
    , "no": "imgs\\1444745515383.png" })

delDev = ({"del": Pattern("imgs\\1444744322036.png").similar(0.90)})

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
    print "\n--Add network via menu Edit-networks...--\n"
    # find(menubar["edit"]).click(menubar["edit"])
    # find(menu_open["edit"]).find(actions["networks"]).click(actions["networks"])
    find(menubar["window"]).highlight(2).click(menubar["window"])
    find(menu_open["window"]).find(actions["networks"]).click(actions["networks"])
    i = 0
    # print("\n1\n")
    while exists(dialogs["network"]) and i < len(networks):
        for network in networks:
            find(buttons["n_add"]).highlight(2)
            click(buttons["n_add"])
            # print("\n2\n")
            type(dialogs["n_new_name"], network)
            # print("\n3\n")
            wait(0.5)
            find(dialogs["n_new_name"]).find(buttons["n_new_name_ok"]).highlight(2)
            click(buttons["n_new_name_ok"])
            # print("\n4\n")
            i = i+1
    find(buttons["n_add_ok"]).highlight(2).click(buttons["n_add_ok"])
    # print("\n5\n")

###### add device ######
def addDevice():
    print "--add device via menu Edit-add Device...--"
    i = 0
    d = 0
    while exists(toolbar["add_dev"]) and i < len(devices):
        for device in devices:
            # find(menubar["edit"]).click(menubar["edit"])
            # find(menu_open["edit"]).find(actions["add_device"]).click(actions["add_device"])
            click(toolbar["add_dev"])
            wait(0.5)
            type(lineEdits["name"], device)
            type(lineEdits["cert_cn"], certCNs[i])
            type(lineEdits["address"], addresses[i])
            type(lineEdits["port"], port[0])
            i = i+1
            find(buttons["d_add_ok"]).click(buttons["d_add_ok"])
			
###### delete device ######
def deleteDevice():
    print "--delete device--"
    i = 0
    mainWin = dialogs["main"]
    while exists(mainWin) and i < len(devices):
        mainWin = find(mainWin).highlight(1)
        with Region(mainWin):
            below_name_col = find(dev_property["name"]).below()
            below_name_col.highlight(2)
            with Region(below_name_col):
                for device in devices:
                    print 3
                    Settings.OcrTextSearch = True
                    if not exists(device):
                        print "device does not exist"
                    elif exists(device):
                        for dev in findAll(device):
                            click(dev)
                            Region(mainWin).find(delDev["del"]).highlight(2).click(delDev["del"])
                            wait(1)
                            Region(mainWin).find(popups["test"]).find(popups_buttons["yes"]).click(popups_buttons["yes"])
                    i = i+1
    print "\n---done deleting devices---\n"
        
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

def getMyScreen():
    myScreen = getScreen()
    return myScreen
###### script start ######
print ("\ncadmin_test.sikuli script running\n")
cadmin = App("C:\\Program Files (x86)\\Tutus\\CAdmin\\cadmin.exe")
cadmin = cadmin.open()
# print cadmin
wait(2)

# V_0.6.0
if not exists(app["cadmin"]):
    wait(2)
if exists(dialogs["main"]):
    initTestSequence()
elif not exists(dialogs["main"]) and exists(app["cadmin"]):
    # wait(dialogs["main"], 10)
    find(app["cadmin"]).highlight(2).click(app["cadmin"])
    onAppear(dialogs["main"], initTestSequence())
else:
    print("\nCould not find CAdmin application\n")

# V_0.5.5
# if exists(app["cadmin"]) and not exists(dialogs["main"]):
	# find(app["cadmin"]).click(app["cadmin"])	
	# onAppear(dialogs["main"], initTestSequence())
# elif exists(app["cadmin"]) and exists(dialogs["main"]):
    # initTestSequence()
	
print("---script done!")
cadmin.close()
# App.close(cadmin)

# during runtime, at every run, this script auto captures an image of the regions searched
# deleting these images to free up space (optional)
# print("\n---deleting auto-captured images by script---\n")
# imgPath = list(getImagePath())
# for path in imgPath:
    # print "path: ", path
    # for file in os.listdir(path):
        # if file.endswith(".png"):
            # print "file: ", file, " will be deleted!"
            # os.remove(path+file)
        # else:
            # print "no *.png files could be found\n"