# Twitch Chat Bot Boiler Plate

This is a bare bones twitch Chat Bot. It works fine for simply listening to incoming chat messages of the specified channel. You can easily extend this with additional functionality such as custom commands and what not.

**Usage:**

- Initialize a ChatBot object as follows:
```
bot = ChatBot('<channel_name>', '<your_auth_token>', 'your_twitch_display_name')
```

- Start listening to incoming chat messages using the `.listen()` method:
```
bot.listen()
```

**Common pitfalls**

- The display name should be the same as the display name of the user that the auth token belongs to.
- If you'd like to have the ability to read badges of each message(such as bits received, no. of months subscribed), you'll need to acquire the auth token with relevant scopes. Check Twitch's [docs](https://dev.twitch.tv/docs/authentication/#scopes) for further information.
