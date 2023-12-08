import math as m, re

board = list(open("data.txt"))
chars = {
    (r, c): []
    for r in range(len(board))
    for c in range(len(board))
    if board[r][c] not in "01234566789."
}
print(chars)
# print(board)

for r, row in enumerate(board):
    for n in re.finditer(r"\d+", row):
        # print(n.group())
        edge = {
            (r, c) for r in (r - 1, r, r + 1) for c in range(n.start() - 1, n.end() + 1)
        }

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

# print(chars)
# print(edge)
print(
    sum(sum(p) for p in chars.values()),
    sum(m.prod(p) for p in chars.values() if len(p) == 2),
)
