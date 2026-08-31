

#python is interpreted so it run until code works after that it given an error 
#error
def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())


    Ret = Addition(value1,value2)
    print("Addition is : ",Ret)


if __name__ == "__main__":      #starter(is not a function ofc) #execution starts from here
    main()


