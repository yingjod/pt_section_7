i = 1
tup10 = ()
while i <= 5:
    a = eval(input())
    tup10 += (a,)
    i += 1
print(tup10)

print("max of the tuple is", max(tup10))
print("min of the tuple is", min(tup10))
print("sum of the tuple is", sum(tup10))
