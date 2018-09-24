def selection(lst):
    count = 0
    print("Started selection")
    for i in range(len(lst)):
        lowest = lst[i]
        for j in range(i + 1, len(lst)):
            count += 1
            if lowest > lst[j]:
                lowest, lst[j] = lst[j], lowest
        lst[i] = lowest
    return lst, count

if __name__ == "__main__":
    print(selection([9, 1, 4, 10, -1]))

