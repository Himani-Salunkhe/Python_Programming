def Addition(No1,No2):
    #Ans = 0....when you need the variable you can create the variable
    Ans = No1 + No2
    return Ans



def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())


    Ret = Addition(value1,value2)
    print("Addition is : ",Ret)


if __name__ == "__main__":      #starter(is not a function ofc) #execution starts from here
    main()


