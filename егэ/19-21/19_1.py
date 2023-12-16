def moves(s):
    return s + 1, 2*s


def game(s):
    if any(x >= 129 for x in moves(s)):
        return "WIN1"  # выигрышная позиция за 1 ход
    if all(game(x) == "WIN1" for x in moves(s)):
        return "LOSS1"  # проигрышная позиция за 1 ход


for s in range(1, 129):
    if game(s) == "LOSS1":
        print(s)
