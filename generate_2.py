import selection, insertion, shellsort
import time
import copy
import csv

def task2():
    for i in range(17, 18):
        lst = [i for i in range(2**i)]
        print(lst)

        start = time.time()
        insertion_op = insertion.insertion(copy.deepcopy(lst))[1]
        end = time.time()
        insertion_time = end - start

        start = time.time()
        selection_op = selection.selection(lst)[1]
        end = time.time()
        selection_time = end - start

        start = time.time()
        shell_op = shellsort.shell(lst)[1]
        end = time.time()
        shell_time = end - start

        with open("task2_op.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_op)] + ['{}'.format(insertion_op)] + ['{}'.format(shell_op)])

        with open("task2_time.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_time)] + ['{}'.format(insertion_time)] + ['{}'.format(shell_time)])

task2()