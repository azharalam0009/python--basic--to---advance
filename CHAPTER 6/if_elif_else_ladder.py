a=int(input("enter your age:"))

if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering invalid negative age:")

elif(a==0):
    print("you are entering 0 which is not valid age")

else:
    print("you are below the age of constant")
    print("end of program")