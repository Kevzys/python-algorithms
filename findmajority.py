def majority(string):
    letters = []
    letters_count = []
    total_count = 0
    for x in string:
        total_count += 1
        if x not in letters:
            letters.append(x)
            letters_count.append(1)
        else:
            i = letters.index(x)
            letters_count[i] += 1

    m = max(letters_count)

    if m > (total_count / 2):
        return 'majority exists'

    return 'no majority'

print(majority('aba'))
