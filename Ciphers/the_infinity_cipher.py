d = {
    0: ["a", "f", "g", "l", "q", "r", "w"],
    2: ["b", "m", "x"],
    6: ["h", "s"],
    12: ["c", "n", "y"],
    20: ["i", "t"],
    30: ["d", "o", "z"],
    42: ["j", "u"],
    56: ["e", "p"],
    72: ["k", "v"]
}


def dinf_cipher(inp):
    inp = inp.split(".")
    x = []
    for i in inp:
        x.append(i)
    final = []
    for i in x:
        t = (int(i) // 125571)
        final.append(t)
    result = []
    for i in final:
        t = ''.join(d[i])
        result.append(t)
    return result


def einf_cipher(inp):
    inp = inp.split(".")
    inp = ''.join(inp)
    res = []
    for i in inp:
        for j in d:
            if i in d[j]:
                res.append(j)
    return res
