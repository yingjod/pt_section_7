color_dict = {}
while True:
    key = input("key:")
    if key == "end":
        break
    value = input("value:")
    color_dict[key] = value

sorteddict = sorted(color_dict)
for i in sorteddict:
    print("%s:%s" % (i, color_dict[i]))
