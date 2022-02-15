


def search(tab, target, value):
    for i in tab:
        if i[2] == value and i[3] == target:
            return i
    return False


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
    tab = []
    max_value = 0
    for y in range(0, len(plateau)):
        for x in range(0, len(plateau[y])):
            if plateau[y][x] == -1:
                eval_black = evalAllDirection(plateau, x, y, 1)
                eval_white = evalAllDirection(plateau, x, y, 0)
                if eval_black > 2.0:
                    tab = stat_exc(eval_black, x, y, tab, 1)
                elif eval_white > 2.0:
                    tab = stat_exc(eval_white, x, y, tab, 0)
                if len(tab) > 0 and tab[-1][2] > max_value:
                    max_value = tab[-1][2]
                # plateau[y][x] = evalAllDirection(plateau, x, y, 1)
    for i in tab:
        print("x: ", i[0], " y: ", i[1], " Value: ", i[2], " Target: ", i[3])
    print()
    print("Max value: ", max_value)
    print()
    filtered = []
    if max_value == 0:
        if plateau[int(len(plateau) / 2)][int(len(plateau[0]) / 2)] == -1:
            filtered.append([int(len(plateau[0]) / 2), int(len(plateau) / 2), 21, color])
        else:
            filtered.append([0, 0, 21, color])
    else:
        for i in tab:
            if i[2] == max_value:
                filtered.append(i)

    if is_me_turn and max_value == 10000:
        find = search(tab, color, 10000)
        if find:
            return [find]
        else:
            return [tab[0]]
    return filtered


def ia(map, color):
    res = evalMap(map, True, color)
    for i in res:
        print("x: ", i[0], " y: ", i[1], " Value: ", i[2], " Target: ", i[3])
    return int(res[0][0]), int(res[0][1])