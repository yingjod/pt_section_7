tup1=()
tup2=()

print('create tuple1:')
while True:
    num=eval(input())
    if num == -9999:
        break
    tup1+=(num,)

print('create tuple2:')
while True:
    num=eval(input())
    if num == -9999:
        break
    tup2+=(num,)

tup_comb=tup1+tup2
print('combined tuple before sorting:',tup_comb)

lst_comb=list(tup_comb)
print('combined list after sorting:',sorted(lst_comb))