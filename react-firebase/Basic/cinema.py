class cinema:

    def __init__(self,CinemaHall,Location,ShowTime):
        self.CinemaHall = CinemaHall
        self.Location = Location
        self.ShowTime = ShowTime

    def display(self):
        print "Cinema hall Name :", self.CinemaHall
        print "Location name    :", self.Location
        print "Show Time        :", self.ShowTime

obj1 = cinema("PVR","Forum Mall","4:30 PM")
obj1.display()