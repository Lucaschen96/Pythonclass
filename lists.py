ar=[4242, 23232, 424, 66, 665]

for el in ar:
    print(el)

ar.append('abc')
print(ar)

print(ar[2])
ar[2]='sdsds'
print(ar[2])

print(len(ar))

print(ar.count(66))
ar.insert(2, 24412)

print(ar)
my_set=set(ar)
print(my_set)

l2=[5353,5356,21424,23323]


for i in range(len(l2)):
    print('Element %i at position %i' % (l2[i],i))

l3=[123213,424,'abcc',42424]
print(l3[2][2:])
l5 = [[1, 6, 8], [8, 9, 3], [3, 9, 4]]
print('-----------')
a=0
i=1
for row in l5:
    for el in row:
        a += el
        print(el)
        print(a)
l6=[0,0,0]
for j in range(len(l5)):
    for k in range(len(l5[j])):
        l6[k] += l5[j][k]

print(l6)


l7=[]
for el in l6:
    l7.append(el*2)
print(l7)

s1=set(l7)
print(s1)


d1={'a':'abcva', 'b': 'sdsdd', 'c':'asdasdf'}
print(d1['b'])
