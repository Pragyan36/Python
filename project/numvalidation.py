def Check(a) :
    i = 0
    while i == 0:
        if a<0 or a>255 :
            print("Invalid Input")
            a = int(input(" please!!!Enter a decimal number between 0 and 255"))
            continue
        break    
    return a

def Entry() :
    i = 0
    while i == 0 :
        try :
            n1 = int(input("Enter a decimal number :"))
        except :
            print("Invalid Input! *Enter a decimal number*")
            continue
        break
    n1 = Check(n1)

    while i == 0 :
        try :
            n2 = int(input("Enter second decimal number:"))
        except :
            print("Invalid Input!*Enter a decimal number.*")
            continue
        break  
    n2 = Check(n2)
    
    return n1, n2


    
