from functools import lru_cache


def moves(s):
    return s + 1, 2*s


@lru_cache
def game(s):
    if any(x >= 129 for x in moves(s)):
        return "WIN1"  # выигрышная позиция за 1 ход
    if all(game(x) == "WIN1" for x in moves(s)):
        return "LOSS1"  # проигрышная позиция за 1 ход
    if any(game(x) == "LOSS1" for x in moves(s)):
        return "WIN2"
    if all(game(x) == "WIN1" or game(x) == "WIN2" for x in moves(s)):
        return "LOSS12"


for s in range(1, 129):
    if game(s) == "LOSS12":
        print(s)
