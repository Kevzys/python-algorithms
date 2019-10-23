def numJewelsInStones(J, S):
    count = 0
    for x in S:
        if x in J:
            count = count + 1

    return count
print(numJewelsInStones("aA", "aaAABBBBAAB"))
