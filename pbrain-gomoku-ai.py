#!/usr/bin/env python3

def search(tab, target, value):
    for i in tab:
        if i[2] == value and i[3] == target:
            return i
    return False


def get_all_by_max_value(tab, max_value):
    res = []
    for i in tab:
        if i[2] == max_value:
            res.append(i)
    return res


def vt_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y - rng < 0 or int(plateau[y - rng][x]) != target:
            break
        count += 1
    return count * 0.1


def dtr_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y - rng < 0 or x + rng >= len(plateau[y]) or int(
                plateau[y - rng][x + rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def hr_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if x + rng >= len(plateau[y]) or int(plateau[y][x + rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def dbr_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y + rng >= len(plateau) or x + rng >= len(plateau[y]) or int(
                plateau[y + rng][x + rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def vb_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y + rng >= len(plateau) or int(plateau[y + rng][x]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def dbl_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y + rng >= len(plateau) or x - rng < 0 or int(plateau[y + rng][x - rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def hl_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if x - rng < 0 or int(plateau[y][x - rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def dtl_fct(plateau, x, y, target):
    count = 0
    for rng in range(1, 5):
        if y - rng < 0 or x - rng < 0 or int(plateau[y - rng][x - rng]) != target:  # todo maybe delete >=
            break
        count += 1
    return count * 0.1


def evalAllDirection(plateau, x, y, target):
    vt = vt_fct(plateau, x, y, target)
    dtr = dtr_fct(plateau, x, y, target)
    hr = hr_fct(plateau, x, y, target)
    dbr = dbr_fct(plateau, x, y, target)
    vb = vb_fct(plateau, x, y, target)
    dbl = dbl_fct(plateau, x, y, target)
    hl = hl_fct(plateau, x, y, target)
    dtl = dtl_fct(plateau, x, y, target)

    # print("x: ", x, " y: ", y, " vt: ", vt, " dtr: ", dtr, " hr: ", hr, " dbr: ", dbr, " vb: ", vb, " dbl: ", dbl, " hl: ", hl, " dtl: ", dtl, " Target: ", target)

    if vt + vb >= dtr + dbl and vt + vb >= hr + hl and vt + vb >= dbr + dtl:
        return (vt + vb) + 2
    if dtr + dbl >= vt + vb and dtr + dbl >= hr + hl and dtr + dbl >= dbr + dtl:
        return (dtr + dbl) + 2
    if dbr + dtl >= vt + vb and dbr + dtl >= hr + hl and dbr + dtl >= dtr + dbl:
        return (dbr + dtl) + 2
    return (hr + hl) + 2


def stat_exc(value, x, y, tab, target):
    if value >= 2.4:
        tab.append([x, y, 10000, target])
    else:
        tab.append([x, y, value * 10, target])
    return tab


def evalMap(plateau, is_me_turn, color):
    tab_black = []
    tab_white = []
    max_black = 0
    max_white = 0
    for y in range(0, len(plateau)):
        for x in range(0, len(plateau[y])):
            if plateau[y][x] == -1:
                eval_black = evalAllDirection(plateau, x, y, 1)
                eval_white = evalAllDirection(plateau, x, y, 0)
                if eval_black > 2.0:
                    tab_black = stat_exc(eval_black, x, y, tab_black, 1)
                    if len(tab_black) > 0 and tab_black[-1][2] > max_black:
                        max_black = tab_black[-1][2]
                elif eval_white > 2.0:
                    tab_white = stat_exc(eval_white, x, y, tab_white, 0)
                    if len(tab_white) > 0 and tab_white[-1][2] > max_white:
                        max_white = tab_white[-1][2]
    if is_me_turn:
        if max_black == 10000:
            return [search(tab_black, color, 10000)]
        if max_white == 10000:
            return [search(tab_white, 0, 10000)]
        if max_black == 0:
            if plateau[int(len(plateau) / 2)][int(len(plateau[0]) / 2)] == -1:
                return [[int(len(plateau[0]) / 2), int(len(plateau) / 2), 21, color]]
            else:
                return [[0, 0, 21, color]]
        return get_all_by_max_value(tab_black, max_black)
    else:
        if max_white == 10000:
            return [search(tab_white, color, 10000)]
        if max_black == 10000:
            return [search(tab_black, 1, 10000)]
        if max_white == 0:
            if plateau[int(len(plateau) / 2)][int(len(plateau[0]) / 2)] == -1:
                return [[int(len(plateau[0]) / 2), int(len(plateau) / 2), 21, color]]
            else:
                return [[0, 0, 21, color]]
        return get_all_by_max_value(tab_white, max_white)


def ia(map, color):
    res = evalMap(map, True, color)
    #for i in res:
    #    if i[3] == color:
    #        return int(i[0]), int(i[1])
    return int(res[0][0]), int(res[0][1])


#################################################################
#################################################################
#################################################################


size = 20

map_init = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]


def place_in_map(x, y, id):
    if id == 0:
        map_init[y][x] = 0.0
    if id == 1:
        map_init[y][x] = 1.0
    # for i in map_init:
    #     print(i)


def start(input) -> str:
    if len(input) != 2 or input[1].isdigit() is False:
        return 'ERROR Start command - unsupported size or other error'
    if int(input[1]) != 20:
        return 'ERROR Start command - unsupported size or other error'
    size = input[1]
    return "OK"


def turn(input):
    if len(input) != 3:
        return 'ERROR Turn command - unsupported size or other error'
    if input[1].isdigit() is False or input[2].isdigit() is False:
        return 'ERROR Turn command - unsupported size or other error(2)'
    if int(input[1]) not in range(size) or int(input[2]) not in range(size):
        return 'ERROR Turn command - unsupported size or other error(1)'
    x = int(input[1])
    y = int(input[2])
    place_in_map(x, y, 0)
    x, y = ia(map_init, 1)
    place_in_map(x, y, 1)
    return f'{x},{y}'


def begin(input):
    if len(input) != 1:
        return 'ERROR', 'Begin command - No arguments expected.'
    x, y = ia(map_init, 1)
    return f'{x},{y}'


def board(arg):
    if len(arg) != 1:
        return 'ERROR', 'Board command - No arguments expected.'
    while True:
        inpt = input()
        if inpt == "DONE":
            break
        inpt = inpt.split(',')
        if len(inpt) != 3:
            return 'ERROR'
        try:
            x = int(inpt[0])
            y = int(inpt[1])
            p = int(inpt[2])
        except:
            return "ERROR 1"
        if x not in range(size) or y not in range(size):
            return 'ERROR 1'
        if p != 1 and p != 2:
            return "ERROR 2"
        place_in_map(x, y, 0 if p == 1 else 1)
    x, y = ia(map_init, 1)
    for i in map_init:
        print(i)
    return f'{x},{y}'


def info(input):
    if len(input) != 3:
        return 'ERROR Info command - Invalid arguments.'
    return f'DEBUG {input[1]} {input[2]}'


def end(input):
    if len(input) != 1:
        return 'ERROR End command - No arguments expected.'
    exit(0)


def about(input):
    if len(input) != 1:
        return 'ERROR About command - No arguments expected.'


def run(arg):
    if arg == "":
        print("UNKNOWN")
    input = arg.replace(',', ' ').split()
    if input[0] == "START":
        print(start(input))
    if input[0] == "END":
        print(end(input))
    if input[0] == "TURN":
        print(turn(input))
    if input[0] == "BEGIN":
        print(begin(input))
    if input[0] == "ABOUT":
        print(about(input))
    if input[0] == "INFO":
        print(info(input))
    if input[0] == "BOARD":
        print(board(input))


if __name__ == "__main__":
    # x, y = ia_main.ia(map, 1)
    # print("x: ", x, " y: ", y)
    while True:
        arg = input()
        run(arg)
