import json

# Returns a dictionary of the information contained in a user object, so that
# this data can be stored in the session.  Also removes sensitive information
# (e.g. passwords) and unserializable items (e.g. complex objects).
def dictifyUser(user):
    userDict = user.__dict__ # make dictionary
    removeList = [] # can't change size of list during iteration
    for key in userDict: # loop through each item, deleting if not serializable
        try:
            json.dumps(userDict[key]) # note that we throw this serialization away; it's just to see if we can serialize it
        except TypeError:
            removeList.append(key)

    for key in removeList:
        del userDict[key]

    del userDict['password']
    return userDict
