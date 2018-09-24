def insertion(lst):
    count = 0
    print("Started insertion")
    for i in range(1, len(lst)):
        value = lst[i]
        j = i
        count += 1
        while j > 0 and lst[j-1] > value:
            count += 1
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = value
    return lst, count


def insertion1(lst):
    for i in range(1, len(lst)):
        hm = lst.pop(i)
        for j in range(i - 1, -1, -1):
            if hm > lst[j]:
                lst.insert(j+1, hm)
                break
            elif hm <= lst[j] and not j:
                lst.insert(j, hm)
                break
    return lst

if __name__ == "__main__":
    import random
    import time
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -4, -5, -6]
    # for i in range(1000):
    #     random.shuffle(lst)
    #     if insertion(lst) == lst:
    #         print(True)
    start = time.time()
    insertion([2, 3, 9, 2, 5, 0, 1, 10, 7, 5, 0, 3, 4, 4, 6, 7, 5, 8, 0, 4, 9, 10, 6, 7, 8, 2, 7, 7, 5, 8, 6, 0, 1, 8, 8, 2, 4, 0, 5, 6, 8, 5, 3, 5, 3, 5, 10, 9, 3, 5, 5, 10, 10, 3, 8, 8, 0, 9, 7, 4, 5, 3, 8, 9, 3, 2, 0, 10, 0, 9, 3, 7, 6, 10, 8, 3, 1, 8, 1, 4, 4, 0, 9, 2, 0, 4, 10, 7, 8, 0, 8, 3, 2, 3, 0, 7, 6, 9, 10, 8, 0, 9, 1, 3, 0, 9, 3, 5, 4, 2, 6, 10, 0, 7, 8, 1, 5, 3, 7, 4, 4, 4, 0, 7, 0, 7, 10, 10, 6, 3, 0, 9, 7, 8, 4, 2, 10, 4, 8, 5, 1, 3, 7, 6, 4, 7, 2, 10, 7, 6, 3, 4, 8, 8, 0, 5, 10, 8, 7, 7, 10, 7, 7, 2, 9, 3])
    end = time.time()

    print(end - start)

    start = time.time()
    insertion1([2, 3, 9, 2, 5, 0, 1, 10, 7, 5, 0, 3, 4, 4, 6, 7, 5, 8, 0, 4, 9, 10, 6, 7, 8, 2, 7, 7, 5, 8, 6, 0, 1, 8, 8, 2, 4, 0, 5, 6, 8, 5, 3, 5, 3, 5, 10, 9, 3, 5, 5, 10, 10, 3, 8, 8, 0, 9, 7, 4, 5, 3, 8, 9, 3, 2, 0, 10, 0, 9, 3, 7, 6, 10, 8, 3, 1, 8, 1, 4, 4, 0, 9, 2, 0, 4, 10, 7, 8, 0, 8, 3, 2, 3, 0, 7, 6, 9, 10, 8, 0, 9, 1, 3, 0, 9, 3, 5, 4, 2, 6, 10, 0, 7, 8, 1, 5, 3, 7, 4, 4, 4, 0, 7, 0, 7, 10, 10, 6, 3, 0, 9, 7, 8, 4, 2, 10, 4, 8, 5, 1, 3, 7, 6, 4, 7, 2, 10, 7, 6, 3, 4, 8, 8, 0, 5, 10, 8, 7, 7, 10, 7, 7, 2, 9, 3])

    end = time.time()
    print(end - start)

