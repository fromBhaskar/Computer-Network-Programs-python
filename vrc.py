def rowparity(arr):
    nums = 0
    for item in arr:
        if item == 1:
            nums += 1
            
    if nums % 2 == 0:
        arr.append(0)
    else:
        arr.append(1)
        
    return arr


def colparity(arr1, arr2, arr3):
    temparr = list()
    for i in range(len(arr1)):
        count = 0
        if arr1[i] == 1:
            count += 1
        elif arr2[i] == 1:
            count += 1
        elif arr3[i] == 1:
            count += 1
        if count % 2 == 0:
            temparr.append(0)
        else:
            temparr.append(1)
    return temparr


def rvc(mylist):
    size = len(mylist)
    print(mylist)
    arr1 = mylist[:8]
    arr2 = mylist[8:16]
    arr3 = mylist[16:]

    row1 = rowparity(arr1)
    row2 = rowparity(arr2)
    row3 = rowparity(arr3)
    row4 = colparity(row1, row2, row3)
    result = row1 + row2 + row3 + row4
    return result


mylist = [1] * 24
print(rvc(mylist))

