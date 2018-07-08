#without using set count list of element and print the element and count
list=[2,3,4,22,33,44,44,22,22,11,33,44,44]
list.sort()
list2=[] # store the final result
list3=[] # store the list element without duplicates
print(list)
for i in range(len(list)):
    if list[i] not in list3:
         list3.append(list[i])
    else:
        pass
print(list3,len(list3))
k=len(list3)
for j in range(k):
    if list.count(list[j]) not in list2:
        list2.append((list3[j],list.count(list[j])))

print(list2)
