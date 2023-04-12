import Programm
import Read
import Sentiment
import State
import Twit
import matplotlib.pyplot as plt


if __name__ == '__main__':
    file = Programm.get_file()
    Read.read_twit(f"./Data/{file}")
    Read.read_sentiments("./Data/sentiments.csv")
    Read.read_json("./Data/states.json")

    for twit in Twit.Twit.twits:
        twit.sentiment = Programm.get_twit_sentiment(twit.message, Sentiment.Sentiment.sentiments)
    Twit.Twit.twits.sort()

    for state in State.State.states:
        snt = 0
        for twit in Twit.Twit.twits:
            value = Programm.is_point_inside_polygon(twit.cord_x, twit.cord_y, state.state_polygons)
            if value:
                state.sentiment += twit.sentiment
    State.State.states.sort()

    fig, ax = plt.subplots()
    for polygon in State.State.states:
        color = Programm.get_color(polygon.sentiment)
        Programm.painting_polygons(polygon.state_polygons, ax, color)
    for point in Twit.Twit.twits:
        color = Programm.get_color(point.sentiment)
        Programm.painting_points(point.cord_x, point.cord_y, color)
    plt.show()
