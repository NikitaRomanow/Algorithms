def insertsort(list):
    for i in range(1,len(list)):
        for j in range (i,0,-1):
            if list[j]<list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
            else:
                break
    return list
list = [-1,0,5,-6,35,-5,5,6]
print(list)
insertsort(list)
print(list)