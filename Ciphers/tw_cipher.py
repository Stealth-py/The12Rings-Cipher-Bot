d = {
    0: ['a', 'm', 'y'],
    1: ['b', 'n', 'z'],
    2: ['c', 'o'],
    3: ['d', 'p'],
    4: ['e', 'q'],
    5: ['f', 'r'],
    6: ['g', 's'],
    7: ['h', 't'],
    8: ['i', 'u'],
    9: ['j', 'v'],
    10: ['k', 'w'],
    11: ['l', 'x']
}


def dclock_cipher(inp):
    inp = inp.split('.')
    res = []
    for i in inp:
        res.append(d[int(i)])
    return res

def eclock_cipher(inp):
    inp = inp.split('.')
    inp = ''.join(inp)
    res=[]
    for i in inp:
        for j in d:
            if i in d[j]:
                res.append(j)
    return res
