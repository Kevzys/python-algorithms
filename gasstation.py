def getGas(a,b):
    n = len(a)
    surplus = 0
    deficit = 0
    s_d_difference = 0
    node_tracker = []

    if sum(b) > sum(a):
        return -1
    else:
        for i in range(n):
            if a[i] < b[i]:
                node_tracker.append(False)
                deficit += a[i] - b[i]
            else:
                node_tracker.append(True)
                surplus += a[i] - b[i]
            print(deficit)


    ans_count = 0
    print(node_tracker)
    for ans in node_tracker:
        if ans == True:
            break
        ans_count += 1
    return ans_count

a = [1,1,1,6,1,1,1]
b = [6,1,1,1,1,1,1]

print(getGas(a,b))
