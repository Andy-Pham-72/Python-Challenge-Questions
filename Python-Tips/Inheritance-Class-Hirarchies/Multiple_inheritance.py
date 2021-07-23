class Coder():
    def __init__(self):
        self.name = input('Name_')

class Pythoner():
    def __init__(self):
        self.works = input('Works')

class WebDev(Coder, Pythoner):
    def __init__(self):
        Coder.__init__(self)
        Pythoner.__init__(self)
    def start_new(self):
        print("new.html @ Django")

if __name__ == '__main__':
    web = WebDev()
    web.start_new()