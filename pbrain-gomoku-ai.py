#!/usr/bin/env python3
from typing import Union

size = 0


def start(input) -> str:
    if len(input) != 2 or input[1].isdigit() is False:
        return 'ERROR Start command - unsupported size or other error'
    if int(input[1]) != 20:
        return 'ERROR Start command - unsupported size or other error'
    size = input[1]
    return "OK - everything is good"


def turn(input) -> str:
    if len(input) != 3:
        return 'ERROR Turn command - unsupported size or other error'
    if input[1].isdigit() is False or input[2].isdigit() is False:
        return 'ERROR Turn command - unsupported size or other error'
    if int(input[1]) not in range(size) \
            or int(input[2]) not in range(size):
        return 'ERROR Turn command - unsupported size or other error'
    x = int(input[1])
    y = int(input[2])
    return f'{x},{y}'


def begin(input) -> Union[tuple[str, str], str]:
    if len(input) != 1:
        return 'ERROR', 'Begin command - No arguments expected.'
    x = int(size / 2)
    y = int(size / 2)
    return f'{x}{y}'


def board(input) -> str:
    return "ERROR"


def info(input) -> str:
    if len(input) != 3:
        return 'ERROR Info command - Invalid arguments.'


def end(input) -> str:
    if len(input) != 1:
        return 'ERROR End command - No arguments expected.'
    exit(0)


def about(input) -> str:
    if len(input) != 1:
        return 'ERROR About command - No arguments expected.'


def run(arg) -> None:
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
    while True:
        arg = input()
        run(arg)
