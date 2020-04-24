x = set()
y = set()

print("enter group x's subjects")
while True:
    subject = input()
    if subject == "end":
        break
    x.add(subject)


print("enter group y's subjects")
while True:
    subject = input()
    if subject == "end":
        break
    y.add(subject)


print(x | y)
print(x & y)
print(y - x)
print(x ^ y)
