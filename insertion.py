def insertion(lst):
    count = 0
    for i in range(1, len(lst)):
        value = lst[i]
        j = i
        count += 1
        while j > 0 and lst[j-1] > value:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = value
    return lst, count


if __name__ == "__main__":
    import random

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -4, -5, -6]
    for i in range(1000):
        random.shuffle(lst)
        if insertion(lst) == lst:
            print(True)
