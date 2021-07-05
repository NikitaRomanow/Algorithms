oldlist = [1,7,47,2452,246,26,24557,347,46,8,39,]

def bubble_sort(list):
    last_item = len(list)-1
    for z in range(last_item):
        for x in range(last_item-z):

            if list[x] > list[x+1]:
                list[x], list[x+1] = list[x+1],list[x]
                print(list)

    return list

print("Старый - " , oldlist)
newlist = bubble_sort(oldlist).copy()
print("Новый -", newlist)
