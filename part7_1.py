num=[]

while True:
    n=int(input())
    if n == -9999:
        break
    num.append(n)

num_tuple=tuple(num)
print(num_tuple)
print('lenght:',len(num_tuple))
print('max:',max(num_tuple))
print('min:',min(num_tuple))
print('sum',sum(num_tuple))