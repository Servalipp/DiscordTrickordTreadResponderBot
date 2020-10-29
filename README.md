# A python bot that automatically claims Trickord-Treat discord bot prizes
This is a python script that I made because my friend got more trinkets than me on the discord bot, so I used my 2 braincells to make this little guy.
This will automatically respond to the Trickord-Treat bot by signing into an automated web browser (Selenium) and also spams the channel so that the bots will actually spawn (I tested it, the server has to be active in order for a bot to be summoned)
**WARNING: I (the original creator) am NOT responsible for any damage made with this bot, and any damage or drama that comes from this bot relies solely on the person running or altering the code. I am not held liable.**

###How do I install this?
You have to download the script, and make sure you have <= python 3.7 installed.
Then you need selenium. `pip install selenium` should work.
After that, you need to download Firefox's **GeckoDriver** executable.
This can be found [here](https://github.com/mozilla/geckodriver/releases).
Make sure it is x86_64 (64 bit).
And thats it, you should now be able to run the python script successfully.
Once you run the script it should open up an automated Firefox browser that will open up to the Discord Web Client. From there you log in and go to the server and channel that the bot runs in, then Hit any key in the console and it will start running.

###Known Bugs
- Since it scans the page content for the message "Open the door and greet them with h!trick/h!treat", if a user discovers the bot, (like my friend did) they can exploit it by typing that same message. Through testing ive figured out that USUALLY this doesnt harm the bot, just spam until the message is out of the page. If a bot spawns within this time then it will still get it correct, but ive never actually had a problem on that so I'm sure it might be exploitable.
- For some strange reason, Selenium at least for me, types messages backwards. So with the `spamMessages` array all the messages are backwards (I implemented a fix for this), and with the typing for `h!trick` and `h!treat` it is also hard coded in reverse. I could try to fix this but I can't be bothered.
- It will spam the command until it can see the "Open the door and greet them with h!trick/h!treat", so it might spam a little, I could fix this with a simple cool down but I dont care that much.

###Editable Variables
`maxCounts`, which goes through every "tick" in python, so it counts to at default 550 to send another spam message. You can fiddle around with the variable to adjust the timing to your liking. From what my research says the bot has a 4-6 minute cooldown until its next message is available.
`enableSpam`, a boolean which enables spam or not. The spam automatically will send messages in speed with the `maxCounts` variable. Making this false will disable spam alltogether