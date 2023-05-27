import math
from datetime import datetime


def z1():
    a = int(input("Liczba 1: "))
    b = int(input("Liczba 2: "))
    c = int(input("Liczba 3: "))

    while a + b + c > 0:
        str = ""
        if a > 0:
            a -= 1
            str += "*"
        str += " "
        if b > 0:
            b -= 1
            str += "#"
        str += " "
        if c > 0:
            c -= 1
            str += "$"
        print(str)


def z2():
    a = int(input("a="))
    znak = str(input("operacja: "))
    b = int(input("b="))

    if znak == "+":
        print(a + b)
    elif znak == "-":
        print(a - b)
    elif znak == "*":
        print(a * b)
    elif znak == "/":
        print(a / b)
    elif znak == "?":
        print(int(a / b))
    elif znak == "%":
        print(str((a / b) * 100) + "%")
    elif znak == "sqrt":
        print(math.sqrt(a))
    elif znak == "root":
        print(a ** (1 / b))
    elif znak == "pow":
        print(a ** b)


def z3():
    field = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    isDone = False
    isCross = False
    while not isDone:
        print("  1  2  3")
        for y in range(3):
            line = str(y + 1) + " "
            for x in range(3):
                line += field[y][x] + "  "
            print(line)

        isValid = False

        prompt = ""
        if isCross:
            prompt += "Player Cross"
        else:
            prompt += "Player Circle"

        while not isValid:
            move = input(prompt + " make your move: ").split(" ")
            mx = int(move[0]) - 1
            my = int(move[1]) - 1
            isValid = (field[my][mx] == " ")
            if not isValid:
                print("Invalid move!")

        if isCross:
            field[my][mx] = "X"
            toCheck = "X"
        else:
            field[mx][my] = "O"
            toCheck = "O"

        isCross = not isCross

        winner = ""

        for y in range(3):
            l = 0
            for x in range(3):
                if field[y][x] == toCheck:
                    l += 1
            if l == 3:
                winner = toCheck

        for x in range(3):
            row = 0
            for y in range(3):
                if field[y][x] == toCheck:
                    row += 1
            if row == 3:
                winner = toCheck

        s = 0
        for i in range(3):
            if field[i][i] == toCheck:
                s += 1
        if s == 3:
            winner = toCheck

        s = 0
        for i in range(3):
            if field[i][2 - i] == toCheck:
                s += 1
        if s == 3:
            winner = toCheck

        if winner != "":
            isDone = True
            print(winner + " WINS!")


def encode(input):
    key = 5
    i = 3
    out = ""
    for c in str(input):
        c = ord(c)
        c += key % i
        i += 1
        out += chr(c)
    return out


def decode(token):
    key = 5
    i = 3
    out = ""
    for c in str(token):
        c = ord(c)
        c -= key % i
        i += 1
        out += chr(c)
    return out


def z4():
    prompt = input("Encode - e, Decode - d, Validate - v: ")
    if prompt == "e":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        email = input("E-Mail: ")
        data = input("Data: ")
        toEncode = imie + "," + nazwisko + "," + email + "," + data
        print(encode(toEncode))
    elif prompt == "d":
        token = input("Token: ")
        print(decode(token))
    elif prompt == "v":
        token = input("Token: ")
        decoded = decode(token).split(",")
        date_object = datetime.strptime(decoded[3], '%d-%m-%Y').date()
        if date_object >= datetime.now().date():
            print("Token is valid")
        else:
            print("Token is invalid")


if __name__ == '__main__':
    z4()
