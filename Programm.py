from matplotlib.patches import Polygon
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import File


def get_file():
    while True:
        for file in File.File:
            print(file)
        value = int(input("Select a file: "))
        if 1 <= value <= len(File.File):
            return f"{File.File(value).name}_tweets2014.txt"
            break


def is_point_inside_polygon(x, y, polygon):
    for pol in polygon:
        num_intersections = 0
        for i in range(len(pol)):
            x1, y1 = pol[i]
            x2, y2 = pol[(i + 1) % len(pol)]
            if ((y1 <= y < y2) or (y2 <= y < y1)) and (x > (x1 - x2) * (y - y2) / (y1 - y2) + x2):
                num_intersections += 1
        return num_intersections % 2 == 1


def get_state_sentiment():
    pass


def get_twit_sentiment(message, words):
    sentiment = 0
    for element in words:
        if element.word in message:
            sentiment += element.value
    return sentiment


def painting_polygons(polygons, ax, color):
    for pol in polygons:
        polygon = Polygon(pol, edgecolor='black', facecolor=color)
        ax.add_patch(polygon)
    ax.autoscale()


def painting_points(x, y, color):
    plt.plot(x, y, marker='o', markersize=4, color=color, markeredgecolor='black')


def get_color(sentiment):
    cmap = mcolors.LinearSegmentedColormap.from_list('mood_map', ['blue', 'yellow'])
    norm = mcolors.Normalize(vmin=-1, vmax=1)
    return cmap(norm(sentiment))
