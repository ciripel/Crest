# Crest
Discord Bot that helps keeping impersonators out

Head over to Discord’s [bot portal](https://discordapp.com/developers/applications/), and create a new application.

![Application Page](../assets/001_app.png)

You’ll want to make a note of the Client ID and secret (which you should keep a secret, of course).
However, this isn’t the bot, just the “Application.” You’ll have to add the bot under the “Bot” tab.

![Bot Page 1](../assets/002_bot1.png?raw=true)

Make a note of this token as well, and keep it a secret. Do not, under any circumstances, commit this key to Github.
Your bot will be hacked almost immediately. This is the BOT token that u need inside `params.json`

You will need to activate SERVER MEMBERS INTENT like in the picture underneath.

![Bot Page 2](../assets/003_bot2.png?raw=true)

The bot will need the following permissions (3078)

![Bot Page 3](../assets/004_bot3.png?raw=true)

NOW ADD THE BOT TO YOUR SERVER:

![Invitation Page](../assets/005_invitation_page.png?raw=true)

Copy this link `https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=3078` and replace CLIENTID
with your bot’s client ID, found on the general information tab of the [application page](https://discordapp.com/developers/applications/).


## Step by step installation:
Setting up the bot requires basic knowledge of the command line, which is bash or similar on Linux/Mac, and cmd.exe in Windows

1. Install Python. Crest requires at least Python version 3.7.
2. Clone this git repo, or download it as a zip or whatever
3. Open a terminal and enter the repo with the cd command. Something like `cd Downloads/Crest-main`. Your exact command may differ
4. Run the command `pip install -r requirements.txt`
5. Make a copy of the file `auth.json.example` and name it `auth.json`.
6. Complete the BOT token that u get from Bot Page in Discord Developer Portal.
7. Make a copy of the file `params.json.example` and name it `params.json`.
8. Add your protected members names in the `banned_names` list.
9. Also add the IDs of the protected members in `ignored_ids` list.

**NOTE:If u forget to add the ID of an protected member he will be banned from the server the moment he has a status change.
This is a feature. It allows u to ban ALL members with a desired name for example.**
10. Start Crest: `python3 bot.py`


Enjoy the BOT!
