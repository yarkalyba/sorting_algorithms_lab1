def selection(lst):
    count = 0
    for i in range(len(lst)):
        lowest = lst[i]
        for j in range(i + 1, len(lst)):
            count += 1
            if lowest > lst[j]:
                lowest, lst[j] = lst[j], lowest
        lst[i] = lowest
    return lst, count


def selection1(alist):
    count = 0


    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            count += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return count
if __name__ == "__main__":
    print(selection([9, 1, 4, 10, -1]))

