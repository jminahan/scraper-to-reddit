class Event():
    def __init__(self, **kwargs):
        self.name = None
        self.description = None
        self.url = None
        self.date = None

        self.handleKwArgs(kwargs)

    def handleKwArgs(self, **kwargs):
        infoDict = kwargs.get('infoDict', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.url = kwargs.get('url', None)
        self.date = kwargs.get('date', None)

        if(infoDict):
            self.handleInfoDict(infoDict)

        return

    def handleInfoDict(self, infoDict):
        if(infoDict["name"] is not None):
            self.name = infoDict["name"];

        if(infoDict["description"] is not None):
            self.name = infoDict["description"];

        if(infoDict["url"] is not None):
            self.name = infoDict["url"];

        if(infoDict["date"] is not None):
            self.name = infoDict["date"];