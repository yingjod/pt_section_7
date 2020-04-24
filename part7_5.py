set1 = set()
set2 = set()
set3 = set()
print("input to set1:")
for i in range(5):
    num = int(input())
    set1.add(num)
print("input to sat2:")
for i in range(3):
    num = int(input())
    set2.add(num)
print("input to set9:")
for i in range(9):
    num = int(input())
    set3.add(num)

print("set2 is subset of set1:", set2.issubset(set1))
print("set3 is superset of set1:", set3.issuperset(set1))
