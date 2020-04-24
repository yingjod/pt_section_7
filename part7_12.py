tup20 = ()
while True:
    num = eval(input())
    if num == -9999:
        break
    tup20 += (num,)

print(tup20)

print("length of the tuple is", len(tup20))
print("the first element is ", tup20[0])
print("the last element is ", tup20[len(tup20) - 1])
