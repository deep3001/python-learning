# A tuple is emmutable data type in python 
tt = (2,3,5.5,"deepashu")
tt3 = (4,5,6)
print(tt)

# t = tt.count(5.5)
t = tt.index(5.5)
print(t)

print(tt + tt3)
print(tt * 3)




print(2 in tt)
print(3234 in tt3)
print(len(tt))
print(min(tt))
print(max(tt))