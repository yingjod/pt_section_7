num = set()

while True:
    inp = eval(input())
    if inp == -9999:
        break
    num.add(inp)

print("lenght:", len(num))
print("max:", max(num))
print("min:", min(num))
print("sum:", sum(num))
