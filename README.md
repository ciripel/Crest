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

Bot requires minimum Python 3.7.
Install the required dependencies
```
$ pip install -r requirements.txt
```

Make an `auth.json` file using `auth.json.example` file as an example. Complete the BOT token that u get from Bot Page in Discord Developer Portal.

Make a `params.json` file usint the `params.json.example` as an example.
Add your protected members names in the `banned_names` list.
Also add the IDs of the protected members in `ignored_ids`.
If u forget to add the ID of an protected member he will be banned from the server the moment he has a status change.
This is a feature. It allows u to ban ALL members with a desired name for example.

Enjoy the BOT!
