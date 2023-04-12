class Twit:
    twits = []

    def __init__(self, cord_x, cord_y, time, message, sentiment):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.time = time
        self.message = message
        self.sentiment = sentiment

    def __str__(self):
        return f"X, Y coordinates: {self.cord_x}, {self.cord_y}    Time: {self.time}    Message: {self.message}    " \
               f"Sentiment: {self.sentiment}"

    def __lt__(self, other):
        return self.sentiment < other.sentiment
