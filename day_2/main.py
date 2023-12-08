import re
from typing import Dict

file = open("data.txt", "r")
dataArray = file.read().split("\n")[:-1]

data = [l.split(": ")[1] for l in dataArray]
data_fini = [[line.lstrip().split(" ") for line in re.split(",|;", l)] for l in data]

# for line in dataArray:
# print(data)

somme = 0
for id, game in enumerate(data_fini):
    balls = {"red": 0, "green": 0, "blue": 0}
    brak = False
    for ball in game:
        if int(ball[0]) > balls[ball[1]]:
            # print(id)
            # print(int(ball[0]), balls[ball[1]])
            balls[ball[1]] = int(ball[0])
            # brak = True
            # break

    # if brak:
    # continue
    somme += balls["red"] * balls["blue"] * balls["green"]

print(somme)
