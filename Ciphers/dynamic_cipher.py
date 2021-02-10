d = {
    0.0: ["a", "f", "g", "l", "q", "r", "w"],
    2.24296011: ['b'],
    2.11354513: ['x'],
    5.68361735: ['s'],
    7.66603921: ['h'],
    10.65560694: ['m'],
    13.45776063: ['n'],
    19.36603735: ['c'],
    25.55346405: ['t'],
    33.64440158: ['z'],
    35.37161448: ['i'],
    48.41509337: ['o'],
    62.32179616: ['j'],
    63.93364165: ['y'],
    74.28039042: ['u'],
    101.59192039: ['d'],
    106.83736484: ['v'],
    138.90322963: ['e'],
    189.63825140: ['p'],
    206.18741590: ['k']
}


def dedyna_cipher(inp):
    inp = inp.split(', ')
    res = []
    for i in inp:
        t = ''.join(d[float(i)])
        res.append(d[float(i)])
    return res


def endyna_cipher(inp):
    inp = inp.split('.')
    inp = ''.join(inp)
    res = []
    for i in inp:
        for j in d:
            if i in d[j]:
                res.append(j)
    return res

print(endyna_cipher("arc.op"))