import Twit
import Sentiment
import State
import csv
import json


def read_twit(filename):
    for line in open(filename, "r", encoding="utf-8"):
        if len(line.split("\t")) == 4:
            element = line.split("\t")
            cords = element[0].split(", ")
            twit = Twit.Twit(float(cords[1][:len(cords[1]) - 1]), float(cords[0][1:]), element[2], element[3], 0)
            Twit.Twit.twits.append(twit)


def read_sentiments(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            sentiment = Sentiment.Sentiment(row[0], float(row[1]))
            Sentiment.Sentiment.sentiments.append(sentiment)


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    for state in data:
        polygons = []
        for state_polygon in data[state]:
            polygon = []
            for element in state_polygon:
                if isinstance(element[0], float):
                    polygon.append(tuple(element))
                else:
                    for point in element:
                        polygon.append(tuple(point))
            polygons.append(polygon)
        state_polygon = State.State(state, polygons, 0)
        State.State.states.append(state_polygon)
