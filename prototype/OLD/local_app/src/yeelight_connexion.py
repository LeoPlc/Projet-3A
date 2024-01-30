from yeelight import Bulb, discover_bulbs


def getIpAddr():
    ipAddr = discover_bulbs()
    return ipAddr


def connectObject(ipAddr):
    bulb = Bulb(ipAddr)
    return bulb


def turnBulb(bulb,light_option):
    if light_option == 1 :
        if bulb.get_properties()["power"] == "on": # Trouver comment faire en sorte de vérifier que le bulbe est déjà allumé
            print("Bulb already on")
        else : 
            bulb.turn_on()
    elif light_option == 0:
        if bulb.bulb.get_properties()["power"] == "off":
            print("Bulb already off")
        else: 
            bulb.turn_off()








'''
headers = ['ID', 'IP', 'Name', 'Type']
content = []
properties_headers = ["ID", "Name", "Power", "Brightness", "Saturation", "Music On"]
properties_content = []

def list_info(bulbs, force=False):
    if len(content) > 0:
        content.clear()
    for i in range(0, len(bulbs)):
        content.append([i, bulbs[0]['ip'], bulbs[0]['capabilities']['name'], bulbs[0]['capabilities']['model']])
    return bulbs

def turn_lights(bulbs, event):
    print(tabulate(content, headers, "pretty"))
    try:
        ans = input("\nBulb IDs (separated by space) => ")
        for a in ans.split(" "):
            bulb = Bulb(bulbs[int(a)]['ip'])
            if event == "off":
                bulb.turn_off()
            else:
                bulb.turn_on()
    except Exception as e:
        print(e)
        
def adjust_brightness(bulbs):
    print(tabulate(content, headers, "pretty"))
    try:
        ans = input("\nBulb IDs (separated by space) => ")
        bright = input("Brightness level => ")
        for a in ans.split(" "):
            bulb = Bulb(bulbs[int(a)]['ip'])
            bulb.set_brightness(int(bright))
    except Exception as e:
        print(e)

def list_bulb_properties(bulbs):
    if len(properties_content) > 0:
        properties_content.clear()
    for i in range(0, len(bulbs)):
        bulb = Bulb(bulbs[0]['ip'])
        props = bulb.get_properties()
        properties_content.append([i, props['name'], props['power'], props['bright'], props['sat'], props['music_on']])
        

def showMenu():
    print("""
    [5] - Adjust brightness
    [4] - Turn on lights
    [3] - Turn off lights
    [2] - List Bulb Properties
    [1] - List bulbs
    [0] - Exit
    [F] - Force Bulb Reload
    """)
    
    # Get user option
    ans = input("Option => ")
    if ans == "0" or ans.lower() == "exit":
        pass
    elif ans == "1":
        # execute action
        showMenu()
    elif ans == "2":
        # execute action
        showMenu()
    else:
        print("Select a valid option")
        showMenu()
'''
