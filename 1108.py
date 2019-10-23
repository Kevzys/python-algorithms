
def defangIPaddr(address):
    y = ''
    for x in address:
        if x is ".":
            x = "[.]"

        y = y + x
    return y

a = "1.1.1.1"
print(defangIPaddr(a))
