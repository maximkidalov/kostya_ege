from functools import lru_cache


def moves(h):
    a, b = h  # кортеж h
    return (a + 1, b), (a, b + 1), (a*2, b), (a, b*2)


@lru_cache(None)
def game(h):
    if sum(h) >= 62:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if any(game(m) == "P1" for m in moves(h)):
        return "B1"


for s in range(1, 52):
    if game((10, s)) is not None:
        print(s, game((10, s)))