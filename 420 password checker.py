def strongPassChecker(string):
    hasDigit = False
    hasUpper = False
    hasLower = False

    filler = ''

    things_wrong = 0
    triple_count = 0


    if len(string) < 6:
        things_wrong += 6 - len(string)
    if len(string) > 20:
        things_wrong += len(string) - 20

    for value in string:
        if value.islower():
            hasLower = True
        if value.isupper():
            hasUpper = True
        if value.isdigit():
            hasDigit = True

        if value in filler:

            triple_count += 1
            if triple_count == 3:
                things_wrong += 1
                filler = ''
            else:
                filler += value
        else:
            filler = ''
            filler += value

    if hasLower == False:
        things_wrong +=1
    if hasUpper == False:
        things_wrong +=1
    if hasDigit == False:
        things_wrong +=1

    return things_wrong

print(strongPassChecker('mmm'))
