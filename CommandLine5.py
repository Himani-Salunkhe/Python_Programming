import sys  #system

if(len(sys.argv)==3):
    No1 = int(sys.argv[1])       #command line input
    No2 = int(sys.argv[2])       #command line input
else:
    print("Invalid number of arguments")

    
Ans = No1 + No2
print("Addition is : ",Ans) 