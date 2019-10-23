def isNumber(string):
    OPERATOR = '+-/'
    DECIMAL = '.'
    ALPHA = 'abcdfghijklmnopqrstuvwxyz'
    filler = ''
    count_decimal = 0
    count_operator = 0
    count_negative_e = 0

    has_e = False

    if string in ALPHA:
        return False

    for value in string:
        if value == 'e':
            if has_e == True:
                return False
            else:
                has_e = True

        if value in OPERATOR and has_e == False:
            count_operator += 1
            if count_operator > 1:
                return False
        if value in DECIMAL and has_e == False:
            count_decimal += 1
            if count_decimal > 1:
                return False


        if has_e:
            filler = filler + value
            if value in OPERATOR:
                if value == '-':
                    count_negative_e +=1
                    if count_negative_e > 1:
                        return False
                else:
                    return False
            if value in DECIMAL:
                return False

    if filler == 'e':
        return False

    return True

print(isNumber('-2.5e-4'))
