from tkinter import *
from heapq import heappop, heappush

HEIGHTS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
HEIGHT_MAP = []
START_X = 0
START_Y = 0
END_X = 0
END_Y = 0
with open("Day12_input.txt", "r") as f:
    i = 0
    for row in f:
        j = 0
        row = row.strip()
        row_elevations = []
        for height in row:
            if height == "S":
                START_X = i
                START_Y = j
                row_elevations.append(0)
            elif height == "E":
                END_X = i
                END_Y = j
                row_elevations.append(25)
            else:
                row_elevations.append(HEIGHTS.index(height))
            j += 1
        HEIGHT_MAP.append(row_elevations)
        i += 1
print("START { X =",START_X,": Y =",START_Y,"}")
print("END { X =",END_X,": Y =",END_Y,"}")

'''
    For this solution, since I've been learning graphs in university,
and I am so done with doing exercises on them, I use William Y. Feng's
algorithms and visualize them myself.

Check him out: https://www.youtube.com/@WilliamYFeng
Also link to the video: https://youtu.be/sBe_7Mzb47Y
'''

def neighbors(x, y):
    # The list is directions where we can go.
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xx = x + dx
        yy = y + dy
        # if not in bounds
        if not (0 <= xx < i and 0 <= yy < j):
            continue
        # if we can get there
        if HEIGHT_MAP[xx][yy] + 1 >= HEIGHT_MAP[x][y]:
            yield xx, yy

visited = [[False] * j for _ in range(i)]
heap = [(0, END_X, END_Y)]
options = []
while True:
    steps, x, y = heappop(heap)
    if visited[x][y]:
        continue
    visited[x][y] = True
    # we reached end
    if HEIGHT_MAP[x][y] == 0:
        print(steps)
        break

    for xx, yy in neighbors(x, y):
        heappush(heap, (steps + 1, xx, yy))