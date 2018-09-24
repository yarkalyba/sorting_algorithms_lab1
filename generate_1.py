# №1
## 2**7

### generate a list
import random
import selection, insertion, shellsort
import time
import copy
import csv

def task1():
    for i in range(15, 17):
        selection_time = 0
        insertion_time = 0
        shell_time = 0

        selection_op = 0
        insertion_op = 0
        shell_op = 0
        for j in range(10):
            lst = [random.randint(0, 10) for i in range(2**i)]
            print(lst)

            start = time.time()
            insertion_op += insertion.insertion(copy.deepcopy(lst))[1]
            end = time.time()
            insertion_time += end - start


            start = time.time()
            selection_op += selection.selection(lst)[1]
            end = time.time()
            selection_time += end - start


            start = time.time()
            shell_op += shellsort.shell(lst)[1]
            end = time.time()
            shell_time += end - start

        with open("task1_op.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_op/10)] + ['{}'.format(insertion_op/10)] + ['{}'.format(shell_op/10)])

        with open("task1_time.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_time/10)] + ['{}'.format(insertion_time/10)] + ['{}'.format(shell_time/10)])


task1()
