class Trip:

    def __init__( self, user, name, city, date, duration, review, id=None ):
        self.user = user
        self.name = name
        self.city = city
        self.date = date
        self.duration = duration
        self.review = review
        self.id = id