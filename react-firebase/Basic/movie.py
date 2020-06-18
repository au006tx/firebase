class movie:

    def __init__(self,MovieName,Actor,Language,Type):
        self.MovieName = MovieName
        self.Actor = Actor
        self.Language = Language
        self.Type = Type

    def display(self):
        print "Movie Name :", self.MovieName
        print "Actor Name :", self.Actor
        print "Language   :", self.Language
        print "Type       :", self.Type

obj1 = movie("Tiger Zinda hai","Salman Khan","Hindi","Action")
obj1.display()