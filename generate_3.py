import selection, insertion, shellsort
import time
import copy
import csv

def task3():
    for i in range(7, 21):
        lst = [-i for i in range(2**i)]
        print(lst)
        start = time.time()
        insertion_op = insertion.insertion(copy.deepcopy(lst))[1]
        end = time.time()
        insertion_time = end - start

        start = time.time()
        selection_op = selection.selection(copy.deepcopy(lst))[1]
        end = time.time()
        selection_time = end - start

        start = time.time()
        shell_op = shellsort.shell(copy.deepcopy(lst))[1]
        end = time.time()
        shell_time = end - start

        with open("task3_op_2.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_op)] + ['{}'.format(insertion_op)] + ['{}'.format(shell_op)])

        with open("task3_time_2.csv", 'a') as file:
            results_writer = csv.writer(file, delimiter=',')
            results_writer.writerow(['{}'.format(i)] + ['{}'.format(selection_time)] + ['{}'.format(insertion_time)] + ['{}'.format(shell_time)])

task3()