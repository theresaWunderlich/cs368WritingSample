# generates personalized, time-sensitive greeting
import datetime

def get_greeting(name):
    # get the current hour to make the greeting time-sensitive.
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        greeting_prefix = "Good morning"
    elif current_hour < 18:
        greeting_prefix = "Good afternoon"
    else:
        greeting_prefix = "Good evening"

    # basic greeting format.
    return f"{greeting_prefix}, {name}!"