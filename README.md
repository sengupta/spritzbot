# Spritzbot

Spritzbot is a boilerplate for creating bots to automate actions based on events
in a user's Twitter timeline. It works on streaming API, hence tends to be much
faster to process tweets and consumes less API calls than the old polling
method.

## Installation:

Download the source into a directory, and run these commands inside the same
directory:

	$ virtualenv --distribute --no-site-packages venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt

Finally, inside bot source directory, 

	$ cp config_example.py to config.py

and update the following:

	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	ACCESS_TOKEN = ''
	ACCESS_TOKEN_SECRET = ''

with credentials you get from [dev.twitter.com](http://dev.twitter.com/) after
creating your app and getting your access token.

## Usage:

	$ python run.py

This will execute the app and start streaming. Events will be handed over to
plugins as and when they come in. 

## Authoring Plugins:

Plugins are stored in the plugins/ directory, add a new module with the
following functions:

	commands()
	process()

commands() returns a list of dicts that tell spritzbot what kind of events your
plugin can handle, and also a compiled list of triggers that are matched before
sending the event to your plugin. The format is like this:

    def commands():
        return [
                {
                    'type':'friends',
                    'triggers':[re.compile('.*')],
                    'field':'all',
                }
               ]


process() will take a single argument, the event/status, and process it.
Whatever it returns, is _currently_ printed out to console. This behaviour may
change.

	def process(status):
   		return "%s: %s" %(status['user']['screen_name'], status['text'])
    

That is all!

~hiway
