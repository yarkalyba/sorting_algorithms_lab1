import matplotlib.pyplot as plt
import csv


x_sel = []
y_sel = []

x_ins = []
y_ins = []

with open("task4_op.csv", 'r') as file:
    plots = csv.reader(file, delimiter=',')
    for row in plots:
        y_sel.append(int(row[1]))
        x_sel.append(int(row[0]))

        y_ins.append(int(row[2]))
        x_ins.append(int(row[0]))

plt.plot(x_sel, y_sel, label='selection')
plt.xlabel('length')
plt.ylabel('operations')
plt.title('Elements from set {1, 2, 3}')
plt.legend()
plt.show()

plt.plot(x_ins, y_ins, label='insertion')
plt.title('Elements from set {1, 2, 3}')
plt.legend()
plt.show()
