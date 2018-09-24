def shell(lst):
    count = 0
    print("Started shell sort")
    gap = len(lst)//2
    while gap > 0:
        for i in range(gap, len(lst)):
            value = lst[i]
            j = i
            count += 1
            while j >= gap and lst[j - gap] > value:
                count += 1
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = value
        gap = gap//2
    return lst, count

if __name__ == "__main__":
    import random
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -4, -5, -6]
    for i in range(1000):
        random.shuffle(lst)
        if shell(lst) == lst:
            print(True)

