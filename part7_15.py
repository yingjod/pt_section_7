dict10 = {}

while True:
    print("key=", end="")
    key = eval(input())
    print("value=", end="")
    v = eval("input()")

    if key != -9999:
        dict10[key] = v
    else:
        break

print(dict10)
