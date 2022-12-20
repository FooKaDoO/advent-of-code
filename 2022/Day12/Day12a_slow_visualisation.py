from tkinter import *
from heapq import heappop, heappush
from queue import Queue
import time
import threading
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

# VISUALISATION:

# Create frame and initialize cell size
frame = Tk()
frame.title("Height map")
frame.resizable(False, False)
frame.geometry("1300x350")
heights = Canvas(frame, width=1300, height=350, background="white")
heights.place(x=0,y=0)
cell_size = 8
# Method to get from rgb to hex
def RGB(rgb):
    return '#%02x%02x%02x' % rgb
def makeSquares(path):
    # Clear
    heights.delete('all')
    # Add squares
    for x in range(i):
        for y in range(j):
            height_value = int(HEIGHT_MAP[x][y] * 10.2)
            blue = 0
            if (x, y) in path or (x, y) == (END_X, END_Y):
                blue = 255
            color = RGB((height_value, 255 - height_value,blue))
            heights.create_rectangle(5 + y * cell_size, 5 + x * cell_size, 5 + (y + 1) * cell_size,
                                     5 + (x + 1) * cell_size, fill=color)


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
        if HEIGHT_MAP[xx][yy] <= HEIGHT_MAP[x][y] + 1:
            yield xx, yy

visited = [[False] * j for _ in range(i)]
heap = [(0, START_X, START_Y)]
makeSquares([(START_X, START_Y)])
nextSquare = Queue()

def visualise():
    while nextSquare.qsize() == 0:
        time.sleep(1)
    x, y = nextSquare.get()
    # create square
    height_value = int(HEIGHT_MAP[x][y] * 10.2)
    color = RGB((height_value, 255 - height_value, 255))
    heights.create_rectangle(5 + y * cell_size, 5 + x * cell_size, 5 + (y + 1) * cell_size,
                             5 + (x + 1) * cell_size, fill=color)

    frame.after(10, visualise)

def while_thread():
    while True:
        steps, x, y = heappop(heap)
        # visualised_path.append((x, y))
        if visited[x][y]:
            continue
        visited[x][y] = True
        # display current path
        nextSquare.put((x, y))

        # we reached end
        if (x, y) == (END_X, END_Y):
            print(steps)
            break

        for xx, yy in neighbors(x, y):
            heappush(heap, (steps + 1, xx, yy))

t1 = threading.Thread(target=while_thread)
t1.start()
frame.after(200, visualise)

frame.mainloop()