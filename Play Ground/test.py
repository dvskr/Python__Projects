
dict={"k1":"v1","k2":"v2"}

list=[1,2,3]
newdict={key:value for key,value in dict.items()}
newlist=[newitem for newitem in list]
print(newdict)
print(newlist)