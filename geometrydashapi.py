import requests, sys

sys.version

__version__ = "2.25.1"
MIN_PYTHON = (2, 25, 1)
if sys.version_info < MIN_PYTHON:
    sys.exit("ERROR: Python %s.%s.%s% or later is required" % MIN_PYTHON)

def profileComment(comment, username, password):
    data = [("comment", str(comment)), ("username", str(username)), ("accountID", user(str(username))["accountID"]), ("password", str(password))]
    pc = requests.post("https://gdbrowser.com/postProfileComment", data=data)
    return pc.text

def user(username):
    userdata = requests.get("https://gdbrowser.com/api/profile/" + str(username)).json()
    if userdata == -1:
        userdata = "ERROR: failed to find the user"
        return False
    else:
        return userdata

def level(levelID):
    leveldata = requests.get("https://gdbrowser.com/api/level/" + str(levelID)).json()
    if leveldata == -1:
        userdata = "ERROR: failed to find the level"
        return False
    else:
        return leveldata

def leaderboard(type):
    if type == "stars":
        lbdata = requests.get("https://gdbrowser.com/api/leaderboard").json()
    elif type == "cps":
        lbdata = requests.get("https://gdbrowser.com/api/leaderboard?creator").json()
    else:
        lbdata = "Can only use these types: 'stars' and 'cps'"
    if lbdata == -1:
        lbdata = "ERROR: failed to get the leaderboard"
        return False
    else:
        return lbdata

def songV(songID):
    song = requests.get("https://gdbrowser.com/api/song/" + str(songID)).text
    if song == "true":
        return True
    elif song == "false":
        return False
    else:
        print("ERROR: failed to find the song")
        return False

if __name__ == "__main__":
    print(user("robtop"))
    print(level(128)["name"])
    print(leaderboard(type="cps"))
    print(songV(1))