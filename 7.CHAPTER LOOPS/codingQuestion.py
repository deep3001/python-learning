# Print numbers from 1 to 10.

for i in range(1,10):
    print(i)

# 2.Print all odd numbers between 1 to 50.

for i in range(1,50):
    if i%2==0:
        continue
    print(i)

# Print all even numbers between 1 to 50.
for i in range(1,50):
    if i%2==0:
        print(i)

# 4.Find the sum of first 10 natural numbers.
sum = 0
for i in range(11):
     sum+=i
print(sum)
print("=============")
# =================================

# userInput = int(input("Please enter any number"))

# # i = 0:
# for l in range(11):
#     print(l*userInput)


# 5.Print all characters of a given string one by one.

strings = "Sudama Soni is my father"

for i in strings:
    print(i)


# 6.Count how many vowels are present in a given string.

# strings = "SudamaSoni"

# for i in strings:
#     if "a" or "e" or "i" or "o" or "u" in strings:
        

# 7.Reverse a string using a for loop.


strings = "SudamaSoni"

for s in reversed(strings):
    print(s)


# Print the square of each number from 1 to 10.


square = [x**2 for x in range(11) ]
print(square)
print("end of the program")


# Print numbers from 1 to 100 that are divisible by both 3 and 5.

# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         print(i)

# Find the sum of all even numbers in a given list.
# li = [1,2,3,4,5,6,7]
# sum =0
# for i in li:
#     if i%2==0:
#         sum+=i
# print(sum)



# Count positive, negative, and zero numbers in a list.

# i dont know this quesiton 


# Find the largest number in a list using a for loop.

# i dont know



li = [1,2,3,4,5,6,7]

largest = li[0]

for i in li:
    if i>largest:
        print(i)