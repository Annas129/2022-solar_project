import matplotlib.pyplot as plt
import csv

def graph_Vt():
    t = 0
    X1 = []
    Y1 = []
    with open("graph.txt") as output_file:
        for line in output_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            t += float(line.split()[0])
            X1.append(t)
            Y1.append(float(line.split()[2]))
    plt.plot(X1, Y1)
    plt.title('planet speed(time)')
    plt.xlabel('t')
    plt.ylabel('V')
    plt.savefig('Vt.png')
    plt.show()


def graph_rt():
    t = 0
    x = []
    y = []
    with open("graph.txt") as output_file:
        for line in output_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            t += float(line.split()[0])
            x.append(t)
            y.append(float(line.split()[1]))
    plt.plot(x, y)
    plt.title('planet r(time)')
    plt.xlabel('t')
    plt.ylabel('r')
    plt.savefig('rt.png')
    plt.show()


def graph_Vr():
    x = []
    y = []
    with open("graph.txt") as output_file:
        for line in output_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            y.append(float(line.split()[2]))
            x.append(float(line.split()[1]))
    plt.plot(x, y)
    plt.title('planet speed(r)')
    plt.xlabel('r')
    plt.ylabel('V')
    plt.savefig('Vr.png')
    plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")