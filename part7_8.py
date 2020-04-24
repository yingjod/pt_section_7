def compute():
    dic = {}
    while True:
        key = input("key: ")
        if key == "end":
            return dic
        value = input("value:")
        dic[key] = value


print("create dict1:")
dict1 = compute()
print("create dict2:")
dict2 = compute()

merge_dict = dict1.copy()
merge_dict.update(dict2)

sorteddict = sorted(merge_dict)
for i in sorteddict:
    print("%s:%s" % (i, merge_dict[i]))
