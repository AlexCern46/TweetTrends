class State:
    states = []

    def __init__(self, state, state_polygons, sentiment):
        self.state = state
        self.state_polygons = state_polygons
        self.sentiment = sentiment

    def __str__(self):
        return f"State: {self.state}    Polygons: {self.state_polygons}    Sentiment: {self.sentiment}"

    def __lt__(self, other):
        return self.sentiment < other.sentiment
