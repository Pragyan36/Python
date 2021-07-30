def Conversion(decimal):
    bit = []
    counter = 0
    while counter != 8 :
        remainder = decimal%2
        bit.append(remainder)
        decimal = decimal//2
        counter += 1

    return bit
