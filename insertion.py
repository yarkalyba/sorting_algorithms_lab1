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


if __name__ == "__main__":
    import random
    import time

    start = time.time()
    print(insertion([2, 4, 1, 6, 2])[1])
    end = time.time()
    print(end - start)
