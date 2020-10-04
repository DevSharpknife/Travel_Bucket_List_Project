class Trip:

    def __init__( self, user, city, date, duration, review, id=None ):
        self.user = user
        self.city = city
        self.date = date
        self.duration = duration
        self.review = review
        self.id = id