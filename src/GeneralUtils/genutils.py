from datetime import date

def today():
    """
    Will return a dict in the form

        {
            "day" : #,
            "month" : #,
            "year" : #
        }
    """
    today = date.today()
    retDict = {}
    retDict["day"] = int(today.strftime("%d"))
    retDict["month"] = int(today.strftime("%m"))
    retDict["year"] = int(today.strftime("%Y"))

    return retDict


def dayNums(**kwargs):
    """
        rangeOfNextDays is the only possible arg besides no arguments
        can i get a womp womp on no overloading

        TODO: I'm aware this is a dumb way to do it and won't loop. A better way to do
            this would be to get a range of date times but we're a startup and we can't
            go back and fix bugs we know about. Move fast and break things.
    """
    rangeOfNextDays = kwargs.get('rangeOfNextDays', None)

    if(rangeOfNextDays == 0 or rangeOfNextDays == None):
        return [today()["day"]]

    base = today()["day"]
    return [i for i in range(base, base + rangeOfNextDays)]

def monthNum():
    return today()["month"]

def yearNum():
    return today()["year"]