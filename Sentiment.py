class Sentiment:
    sentiments = []

    def __init__(self, word, value):
        self.word = word
        self.value = value

    def __str__(self):
        return f"Word: {self.word}    Value: {self.value}"
