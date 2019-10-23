# to flip image:
#first flip all values
#then not all values
#(essentially xor)
def flipAndInvertImage(a):
    for row in a:
        for i in range(int((len(row)+1)/2)):
            print(-i -1)
            row[i], row[~i] = row[~i] ^1, row[i] ^ 1
    return a

a = [[1,1,0,0,1],[1,0,0,1,1],[0,1,1,1,1],[1,0,1,0,1]]
print(flipAndInvertImage(a))
