#!/usr/bin/env python3
import time

rows, cols = 16, 32

def countNbors(x: int, y: int, c: dict) -> int:
    count = 0
    for i in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if (i == 0 and k == 0):
                continue
            dx = (x + i) % cols
            dy = (y + k) % rows
            key = (dy * cols) + dx
            if (c[key] == 1):
                count += 1
    return count


def update(c: dict) -> dict:
    loc = {}
    for y in range(rows):
        for x in range(cols):
            nbors = countNbors(x, y, c)
            if c[y * cols + x] == 1:
                if nbors == 2 or nbors == 3:
                    loc[y * cols + x] = 1
                else:
                    loc[y * cols + x] = 0
            else:
                if nbors == 3:
                    loc[y * cols + x] = 1
                else:
                    loc[y * cols + x] = 0

    return loc


def display(c: dict):
    print("\033[H\033[2J")
    for y in range(rows):
        row = ""
        for x in range(cols):
            row += "." if c[y * cols + x] == 0 else "x"
        print(row)


def main():
    cells = {}
    for y in range(rows):
        for x in range(cols):
            cells[y * cols + x] = 0

    cells[1] = 1
    cells[34] = 1
    cells[64] = 1
    cells[65] = 1
    cells[66] = 1
    display(cells)
    while True:
        cells = update(cells)
        display(cells)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
