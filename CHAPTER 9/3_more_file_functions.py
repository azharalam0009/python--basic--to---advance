# for read many lines in one times 

f=open("file.txt")

# lines=f.readlines()

# print(lines,type(lines))
# f.close()


# for read line one by one 

line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

line4=f.readline()
print(line4,type(line4))

f.close()
