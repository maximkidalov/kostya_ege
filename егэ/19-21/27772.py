from functools import lru_cache
import sys

sys.setrecursionlimit(150000)


def moves(h):
    a, b = h  # кортеж h
    return (a - 1, b), (a, b - 1), (a//2 + 1, b), (a, b//2 + 1)


@lru_cache(None)
def game(h):
    if h[0] <= 1 or h[1] <= 1:
        return
    if sum(h) <= 20:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if all(game(m) == "P1" for m in moves(h)):
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"


for s in range(11, 100):
    if game((10, s)) is not None:
        print(s, game((10, s)))
