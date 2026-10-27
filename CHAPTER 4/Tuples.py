a=(1,3,6,7)
print(type(a))

a=(1,)
print(type(a))

a=(6,7,4,2,"sameer,False")

a=[0]=65   # error because tuples cannot be changed.

a=(1,45,76,78,"sameer","azhar","sameer")
no= a.count("sameer")
print(no)


a=(1,45,76,78,"sameer","azhar","sameer")
i= a.index("sameer")
print(i)
