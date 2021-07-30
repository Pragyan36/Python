def Add(binary1,binary2):
    sum =[]

    a = binary1[7]
    b = binary2[7]

    s = a^b
    c = a&b
    sum.append(s)

    for i in range(6,-1,-1):
        s = binary1[i]^binary2[i]^c
        c = (binary1[i]&binary2[i])|((binary1[i]^binary2[i])&c)
        sum.append(s)
    if c!=0:
        sum="not 8-bit operation."
        
    return sum
