def b10tob36(num):
    b10num = int(num)
    if b10num == 0:
        return "000"
    res = ""
    while b10num:
        if int(b10num % 36) > 9:
            res = chr(int(b10num % 36) + 55) + res
        else:
            res = str(int(b10num % 36)) + res
        b10num //= 36

    while len(res) < 3:
        res = "0" + res

    return res


def b36tob10(num):
    return str(int(num), 36)
