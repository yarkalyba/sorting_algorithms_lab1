### generate a list
import random
import selection, insertion, shellsort
import time
import copy
import csv

def task4():
    for i in range(7, 21):
        lst = [random.randint(1, 3) for i in range(2 ** i)]
        selection_time = 0
        insertion_time = 0
        shell_time = 0

        selection_op = 0
        insertion_op = 0
        shell_op = 0
        for j in range(10):
            random.shuffle(lst)
            print(j, lst)

            start = time.time()
            insertion_op += insertion.insertion(copy.deepcopy(lst))[1]
            end = time.time()
            insertion_time += end - start


            start = time.time()
            selection_op += selection.selection(copy.deepcopy(lst))[1]
            end = time.time()
            selection_time += end - start


            start = time.time()
            shell_op += shellsort.shell(copy.deepcopy(lst))[1]
            end = time.time()
            shell_time += end - start

        with open("task4_op_2.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(int(selection_op/10))] + ['{}'.format(int(insertion_op/10))] + ['{}'.format(int(shell_op/10))])

        with open("task4_time_2.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_time/10)] + ['{}'.format(insertion_time/10)] + ['{}'.format(shell_time/10)])


task4()
