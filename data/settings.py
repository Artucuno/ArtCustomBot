# Settings for ACB
# ===================

# Show Commands that have been run
commandoutput = True
# Download MDBL Module and enable it
mdbl = False
# Remove help command
helpcmd = False
# Disable commands
commands = ['', '']
# Startup modules
# You can change this to whatever you want just keep 'bot' or you wont be able to do much!
extensions = ['bot', 'mod', 'server', 'fun', 'audio']
# Audio Settings
playing = True # Show Now Playing
DJ = True
# Game Settings
game = ""
gtype = 1 # 1 = Playing, 2 = Listening to, 3 = Watching

# Extra stuff

# Music
if DJ == True:
    # This role can control music
    DJRole = "580683954747736074" # Role ID
else:
    # Dont Edit this
    DJRole = ""
