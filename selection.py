def selection(lst):
    count = 0
    print("Started selection")
    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):
            count += 1
            if lst[lowest] > lst[j]:
                lowest = j
        lst[i], lst[lowest] = lst[lowest], lst[i]
    return lst, count

if __name__ == "__main__":
    import random

    lst = [random.randint(0, 20) for i in range(2**11)]
    print(selection(lst))