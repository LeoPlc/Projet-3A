from yeelight import discover_bulbs, Bulb
import readline

# WiFi

# 1 lampe Xiaomi
# 192.168.1.58


# 2 lampes et 1 prise TAPO



def turnOnNearBulb():
    bulbs = discover_bulbs()
    print(bulbs)

    bulb = Bulb(bulbs[0]['ip'])
    print(bulb)
    bulb.turn_off()
    
    
turnOnNearBulb()

def menu():
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
        menu()
    elif ans == "2":
        # execute action
        menu()
    else:
        print("Select a valid option")
        menu()
        
