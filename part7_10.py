my_dict = {}

while True:
    key = input("key:")
    if key == "end":
        break
    value = input("value: ")
    my_dict[key] = value

search_key = input("search key: ")
print(search_key in my_dict)
