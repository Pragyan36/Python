import numvalidation
import decimaltobinary
import reverse
import binaryaddition
import greeting
import Conclude

greeting.Greeting()
run = "yes"

while(run=="yes"):
    result = numvalidation.Entry()
    n1 = result[0]
    n2 = result[1]

    c1 = decimaltobinary.Conversion(n1)
    c2 = decimaltobinary.Conversion(n2)

    binary1 = reverse.Arrange(c1)
    binary2 = reverse.Arrange(c2)

    sum = binaryaddition.Add(binary1,binary2)

    if not type(sum) is str:
        sum = reverse.GetStr(sum)

    print("The required sum is ",sum)

   
    tocontinue=input("Do you wish to continue???(Yes/No): ")
    if tocontinue=="NO" or tocontinue=="no":
        break

Conclude.conclude() 
