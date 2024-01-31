class ToDo:
    def __init__(self,list):
        self.userId = list[1]["userId"]
        self.id = list[1]["id"]
        self.title = list[1]["title"]
        self.completed=list[1]["completed"]