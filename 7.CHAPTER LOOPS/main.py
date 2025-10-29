# for i in range(1,10):
#     print(i)


# fruits = ["apple","banana","orange","greps","mango"]

# # for i,t in enumerate(fruits):
# #     print(i,t)

# ============================================


# list looping 

# fruits = ["apple","banana","orange","greps","mango"]

# cars = ['tata','suzuki','maruti','kia']

# for x,y in zip(fruits,cars):
#     print(x,y)

# =========================================================================

# list = [4,2,45,3,43,56,67,56,12,3]

# for i in list:
#     if i%2==0:
#         print(i,"is even number")

# ========================================================



# list = [[1,2,3],[4,5,6],[7,8,9]]

# for i in list:
#     for s in i:
#         print(s, end=" ")
#     # print()


# list = [4,2,45,3,43,56,67,56,12,3]

# for i in reversed(list):
#     print(i)


# for i in range(5):
#     if i == 4:
#         break
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(21,30):
#     if i == 23:
#         pass
#     print(i)


list = [4,2,45,3,43,56,67,56,12,3]

for i in sorted(list):
    print(i)


fruits = ["apple","banana","orange","greps","mango"]

for i, x in enumerate(reversed(fruits)):
    print(i,x)