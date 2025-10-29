# age = 18

# if age<18:
#     print("you can vote")
# else:
#     print("you can't vote")

# # =========================================================

# userInput = int(input("please enter your age"))


# if userInput<0 or userInput>=110:
#     print("wrong input")
# elif userInput>=1 and userInput<=12:
#     print("you are childern")
# elif userInput>=12 and userInput<=17:
#     print("you are teenuserInputr")
# elif userInput>=18 and userInput<=109:
#     print("you can vote")
# else:
#     print("program end")

# =========================================================

# Nested If 

# x = 15 

# if x > 10:

#     if x < 20:
#         print("x is between 10 and 20 ")
# else:
#     print("error")

# # Short-Hand if

# a = 5
# b = 10

# print("a is greater thenb ") if a>b else print("b is greater then a")











# scores = [0.91, 0.67, 0.88, 0.95]

# for s in scores:
#     if s >= 0.9:
#         print(f"{s} → Excellent")
#     elif s >= 0.8:
#         print(f"{s} → Good")
#     else:
#         print(f"{s} → Poor")
# ==================================================================

# first = int(input("please enter your first subject marks"))
# second = int(input("please enter your second subject marks"))
# third = int(input("please enter your third subject marks"))


# avg = (100*(first+second+third))/300

# if avg<40:
#     print("you are fail :",avg)
# else:
#     print("you are pass :", avg)

# ----------------------------------------------


# UserInput = str(input("please enter text :"))

# if UserInput == "make a lot of money" or "buy now" or "subscribe this" or "click this":
#     print("this is scam")
# else:
#     print("this is normal text")

# ======================================================



# UserInput = str(input("please enter text :"))

# if len(UserInput)<10:
#     print("less then ten")
# else:
#     print("great then ten")


# =====================================


# list = ["yug","deep","yuv","chintu","deepak"]

# UserInput = str(input("please enter text :"))

# if UserInput in list:
#     print(True)
# else:
#     print(False)
# =========================================


# UserInput = int(input("please enter percentage :"))

# if UserInput<0 or UserInput>100:
#     print("wrong input")
# elif UserInput>90 and UserInput<=100:
#     print("Exellent")
# elif UserInput>80 and UserInput<=90:
#     print("A")
# elif UserInput>70 and UserInput<=80:
#     print("B")
# elif UserInput>60 and UserInput<=70:
#     print("C")
# elif UserInput>50 and UserInput<=50:
#     print("D")
# else:
#     print("Fail")
# =======================================================

UserInput = str(input("please enter text :"))

Lower = UserInput.lower()

if "Harry" in Lower:
    print("this post is talking about harry")
else:
    print("this post not talking about harry")