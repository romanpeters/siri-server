# siri-server

![screenshot](/images/screenshot.png)

Siri Server is a small web server, designed to run on a macOS server or virtual machine.  
It can relay queries to Siri by emulating keyboard presses and accessing the macOS system Siri assistant.
It features a webpage were you can enter your query as well as an API.

# Why?
For instance, if you want to automate running a specific Siri command, this is now only one URL call away.
Most things can already be automated using the Shortcuts app, but that app still lacks an option to run a Siri command directly.
Using Siri Server you can run Siri commands from Shortcuts, cron, or however you like.

# Limitations
Unfortunately Siri doesn't reply yet through Siri Server, it's a one-way communication channel.
Of course this doesn't matter if you can still hear your system's audio output, or if you're using it for commands for which the response doesn't matter (e.g. controlling things in your home).

# Installation
To install the dependencies and start the server, run:
```
pip install -r requirements
python run.py
```
For Siri Server to be able to relay to Siri, 'Type to Siri' must be enabled under System Preferences > Accessibility > Siri.  
The first time you run Siri Server, it will also ask you to allow it to interact with your keyboard.

# Usage
When you've got the system up and running, you can visit Siri Server in your web browser on http://127.0.0.1:5000.
The API can be found at http://127.0.0.1:5000/api.
Here's an example of an API request using curl:  
```
curl -X POST -H "Content-Type: application/json" -d '{"query": "turn the tv off"}' http://127.0.0.1:5000/api/ask
```