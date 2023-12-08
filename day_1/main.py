import re

file = open("data.txt", "r")
dataArray = file.read().split("\n")[:-1]

# SECOND STAR
pattern = re.compile("(1|2|3|4|5|6|7|8|9)")
stringArray = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

somme = 0
for line in dataArray:
    for n in stringArray.keys():
        line = line.replace(n, n[0] + stringArray[n] + n[-1])

    foundList = pattern.findall(line)

    first = foundList[0]
    last = foundList[-1]

    value = int(first + last)
    somme += value

print(somme)
