
# lists - ordered collections of items of any datatype


list1 = ['hello','hi','welcome',3,True]
# print(list1)



# Accessing a specific item in a list


# print(list1[4])  # 0 - Index Position
# print(list1[-1])

# ------------------------------------------------------------------------


#
# print(len(list1))
#
# list2 = [ 'hello' , 9 , True]
# print(type(list2))


# ------------------------------------------------------------------------


# list1[start:end]



# print(list1[0:])  # Start Value to End Value - 1
# print(list1[0:2])


# ------------------------------------------------------------------------



# list1[start:end:jump]


# list1 = [1,2,3,4,5,6,7,8]
# print(list1[0::])
# print(list1[0::2])
# print(list1[::2])


# Some list functions

# list3 = [ 1,2,3,4]
# list3.insert(2,"Hello")   # insert at a particular index
# print(list3)
#
# list3.append('welcome') # insert to the end
# print(list3)
#
# list3.remove(2)  # removes first occurence of the value
# print(list3)


# list4 = ['hello','hi','welcome']
# print("*".join(list4))  # Only possible with lists that contain strings