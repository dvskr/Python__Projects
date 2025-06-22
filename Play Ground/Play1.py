# #Escape character \n for new line

# print("Sathish\nDaggula")

#  r"...." makes escape sequence consider as part of string

# print(r"Sathish\nDaggula")
#
# print("Sathish"[0])
# print("Sathish"[-1])

# type() used to know data type
# print(type(input("Type something to know datatype")))
#
# Type Casting : Changes the data type
#
# op=str(12) #op: "12"
#
# Precedence Rule : () > x**y >mul/div >add/sub (left to right)
#
# #Rounds to nearest integer
#
# print(round(int(input("Type a number to get nearest integer"))))

#round(x,y) x is number and y is nuber of decimal places for round up

#python limitation
# print(150*1.12)

# print(5//2)



#use one more \ in order to interpret as part of string
# print("hello\\")

#multiline syntax

# print("""bdcshbcknsdkcni
# naschikajeclmal
# dandskcmaklm""")

# list=[['a','b'],['c','d']]

# print(list[0][1])

# for i in "sathish":
#     print(i)
#
# list=["sathish"]
#
# for i in list:
#     print(i)
#     print(list.index(i))
#
# dict={
#     "key1":"value1","key2":"value2","key3":"value3","key4":4
# }
#
# #print(dict["key1"])
#
# for key in dict:
#     print(key)
#     print(dict[key])

# dict={
#     "key1":"value1","key2":"value2","key3":"value3","key4":4, "key5":{"key6":"value6"}, "key7":[1,2,3,"abc"]
# }
# for key in dict:
#
#     print(dict[key])

# print(dict["key5"]["key6"])
# print(dict["key7"][0])

# dict={"k1":2,"k2":3,}
#
# print(max(dict,key=dict.get))
#
# print(dict.get("k2"))

#Ineer and outer func

# def outer_fun(c,d):
#     def inner_fun(a,b):
#         return a+b
#     return inner_fun(c,d)
# print(outer_fun(1,2))

#local and global scope

# a=5 #global
# print(a)
#
# def local_fun():
#     a=4 #local
#     print(a)
#
# local_fun()
# print(a)
#
# def access_global_fun():
#     global a
#     a*=2
#     print(a)
#
# access_global_fun()
#
# print(a)





