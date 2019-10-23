def majority(string):
    m = {}

    for x in string:
        if x not in m.keys():
            m.update(x, 1)
        else:
            m[x] +=1
    print(m)

majority('aab')
