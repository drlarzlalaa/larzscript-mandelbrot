#!/usr/bin/env python3
"""Independent Python check of mandelbrot.lz: the same escape-time iteration on the same grid of pixel centres.

    python3 tools/reference.py render XMIN XMAX YMIN YMAX WIDTH HEIGHT MAX   -> the picture
    python3 tools/reference.py stats  XMIN XMAX YMIN YMAX WIDTH HEIGHT MAX   -> "N points, I inside, S steps in all"
    python3 tools/reference.py point RE IM MAX                               -> steps until escape (MAX if none)
"""
import sys


def escape_steps(cr, ci, limit):
    zr = zi = 0.0
    for i in range(limit):
        zr2, zi2 = zr * zr, zi * zi
        if zr2 + zi2 > 4.0:
            return i
        zi = 2.0 * zr * zi + ci
        zr = zr2 - zi2 + cr
    return limit


def glyph(n, limit):
    if n >= limit: return "@"
    for top, g in ((1, " "), (2, "."), (3, ":"), (5, "-"), (8, "="), (14, "+"), (30, "*")):
        if n <= top:
            return g
    return "#"


def grid(xmin, xmax, ymin, ymax, w, h, limit):
    dx, dy = (xmax - xmin) / w, (ymax - ymin) / h
    for row in range(h):
        ci = ymax - (row + 0.5) * dy
        yield [escape_steps(xmin + (col + 0.5) * dx, ci, limit) for col in range(w)]


if __name__ == "__main__":
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == "point":
        print(escape_steps(float(a[0]), float(a[1]), int(a[2])))
    else:
        xmin, xmax, ymin, ymax = map(float, a[:4])
        w, h, limit = map(int, a[4:7])
        rows = list(grid(xmin, xmax, ymin, ymax, w, h, limit))
        if cmd == "render":
            for r in rows:
                print("".join(glyph(n, limit) for n in r))
        else:
            print("%d points, %d inside, %d steps in all" % (w * h, sum(n >= limit for r in rows for n in r), sum(map(sum, rows))))
