funnum = int(input("Enter How many numbers you have to use in the operation:"))


if funnum==2:
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))



    fun = input("Enter your operation :")

    if(fun=="+"):
        print(num1+num2)

    elif(fun=="-"):
        print(num1-num2)

    elif(fun=="x"):
        print(num1*num2)

    elif(fun=="/"):
        print(num1/num2)

    elif(fun=="^"):
        print(num1**num2)
    elif(fun=="root"):
        print(num1**(1/num2))

elif funnum==3:
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    num3 = int(input("Enter 3rd number:"))


    fun = input("Enter your operation :")

    if(fun=="+"):
        print(num1+num2+num3)

    elif(fun=="-"):
        print(num1-num2-num3)

    elif(fun=="x"):
        print(num1*num2*num3)

    

    
elif funnum==4:
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    num3 = int(input("Enter 3rd number:"))
    num4 = int(input("Enter 4th number:"))

    fun = input("Enter your operation :")

    if(fun=="+"):
        print(num1+num2+num3+num4)

    elif(fun=="-"):
        print(num1-num2-num3-num4)

    elif(fun=="x"):
        print(num1*num2*num3*num4)

elif funnum==5:
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    num3 = int(input("Enter 3rd number:"))
    num4 = int(input("Enter 4th number:"))
    num5 = int(input("Enter 5th number:"))
    


    fun = input("Enter your operation :")

    if(fun=="+"):
        print(num1+num2+num3+num4+num5)

    elif(fun=="-"):
        print(num1-num2-num3-num4-num5)

    elif(fun=="x"):
        print(num1*num2*num3*num4*num5)

elif funnum >5 :
    print("There Are Too many Variables to process, Please try a simpler sum.")

input("Function complete, Press Enter key to exit")


