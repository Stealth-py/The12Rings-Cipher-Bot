d = {
    7: ['a', 'm', 'y'],
    33: ['b', 'n', 'z'],
    34: ['b', 'n', 'z'],
    23: ['c', 'o'],
    11: ['d', 'p'],
    15: ['e', 'q'],
    43: ['f', 'r'],
    44: ['f', 'r'],
    39: ['g', 's'],
    29: ['h', 't'],
    21: ['i', 'u'],
    25: ['j', 'v'],
    13: ['k', 'w'],
    35: ['l', 'x']
}


def desec_cipher(inp):
    inp = inp.split('.')
    res = []
    for i in inp:
        t = ''.join(d[int(i) - 3360])
        res.append(t)
    return res


def ensec_cipher(inp):
    inp = inp.split('.')
    inp = ''.join(inp)
    res = []
    for i in inp:
        for j in d:
            if i in d[j]:
                res.append(j)
    return res
