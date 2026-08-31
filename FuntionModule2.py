import Marvellous as MI         #alise(nickname of marvellous)

def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())


    Ret = MI.Addition(value1,value2)
    print("Addition is : ",Ret)


if __name__ == "__main__":      #starter(is not a function ofc) #execution starts from here
    main()


