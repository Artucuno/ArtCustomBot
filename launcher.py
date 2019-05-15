import sys, os
print("[DEBUG] Imported sys, os")
import time
print("[DEBUG] Imported time")
import subprocess
print("[DEBUG] Imported subprocess")
import json
print("[DEBUG] Imported json")
import discord
print("[DEBUG] Imported discord.py")
import time
print("[DEBUG] Imported time")

if discord.__version__ == "0.16.0" or "0.16.12":
    print("[DISCORD] Correct API version | {}".format(discord.__version__))
    time.sleep(2)
else:
    input("[DISCORD] Unusable discord API version :(\nYou need v0.16.0 or v0.16.12 and you have {}".format(discord.__version__))
    exit(10)

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").strip()

def check():
    if os.path.isfile('data/config.json'):
        launch()
    else:
        create()

def create():
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-\n"
          "    ArtCustomBot   \n"
          "-=-=-=-=-=-=-=-=-=-\n\n`")
    print("Enter your bot token!")
    tken = user_choice()
    print("Enter prefix!")
    pref = user_choice()
    print("Enter your discord id!")
    did = user_choice()
    print("[CONSOLE] Creating data files")
    data = {}
    data['Config'] = []
    data['Config'].append({
        'prefix': "{}".format(pref),
        'oid': "{}".format(did),
        'Descript': "ArtCustomBot - https://github.com/Articuno1234/ArtCustomBot"
        })
    with open('data/config.json', 'w') as outfile:
        json.dump(data, outfile)
    time.sleep(1)
    tok = open("data/tken.py", "w+")
    tok.write("token = '{}'".format(tken))
    print("[CONSOLE] Created config file")
    time.sleep(2)
    tok.close()
    data = {}
    data['Config'] = []
    data['Config'].append({
        'ownerid': "{}".format(did),
        'errorchannel': "None"
        })
    with open('data/utils/settings.json', 'w') as outfile:
        json.dump(data, outfile)
    time.sleep(2)
    data = {}
    data['Mdbl'] = []
    data['Mdbl'].append({
        'Active': "False"
        })
    with open('data/mdbl.json', 'w') as outfile:
        json.dump(data, outfile)
    print("[CONSOLE] Created MDBL file")
    time.sleep(1)
    data = {}
    data['Game'] = []
    data['Game'].append({
        'Gme': "",
        'Type': 1
        })
    with open('data/game.json', 'w') as outfile:
        json.dump(data, outfile)
    print("[CONSOLE] Created Game Status file (Default game: None, Type: 1)")
    time.sleep(2)
    launch()
        
# description='ArtCustomBot - https://github.com/Articuno1234/ArtCustomBot'

def launch():
    clear_screen()
    print("-=-=-=-=-=-=-=-=-=-\n"
          "    ArtCustomBot   \n"
          "-=-=-=-=-=-=-=-=-=-")
    print("1. Run\n"
          "2. Delete Bot (NOT RECOMMENDED!)\n"
          "3. Update Bot help description\n"
          "4. Update Bot")
    choice = user_choice()
    if choice == "1":
        subprocess.call(("python3", "data/run.py"))
    if choice == "2":
        os.remove("data/config.json")
        os.remove("data/tken.py")
        input("[CONSOLE] Removed all bot data")
        exit(10)
    if choice == "3":
        desc()
    if choice == "4":
        update()
    else:
        exit(10)

def desc():
    clear_screen()
    if os.path.isfile('data/config.json'):
        with open('data/config.json') as json_file:  
            data = json.load(json_file)
            for p in data['Config']:
                print("Enter a description (Current: {})".format(p['Descript']))
                choice = user_choice()
                if choice == "":
                    launch()
                else:
                    data = {}
                    data['Config'] = []
                    data['Config'].append({
                        'prefix': "{}".format(p['prefix']),
                        'oid': "{}".format(p['oid']),
                        'Descript': "{}".format(choice)
                        })
                    with open('data/config.json', 'w') as outfile:
                        json.dump(data, outfile)
                    print("[CONFIG] Updated Description to {}".format(choice))
                    launch()
    else:
        check()

def update():
    try:
        code = subprocess.call(("git", "pull", "--ff-only"))
    except FileNotFoundError:
        print("\nError: Git not found. It's either not installed or not in "
              "the PATH environment variable like requested in the guide.")
        return
    if code == 0:
        print("\nArtCustomBot has been updated")
    else:
        print("\nArtCustomBot could not update properly.")

check()
