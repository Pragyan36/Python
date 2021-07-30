def Arrange(a):
    Binary = []

    for i in range(len(a)-1,-1,-1) :
        Binary.append(a[i])
        
    return Binary

def GetStr(a):
    BinaryNum = ""

    for i in range(len(a)-1,-1,-1) :
        BinaryNum = BinaryNum + str(a[i])
        
    return BinaryNum
