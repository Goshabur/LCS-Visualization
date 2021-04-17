import random
from interactive_visualization.animation_utils import animate_list
from IPython.display import Code
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


def fill_cell(i, j, color, ax):
    ax.fill([i, i, i + 1, i + 1, i], [j, j + 1, j + 1, j, j], color=color)


def draw_filling(filling, a, b, x, y, bool):
    if filling is not None:
        n = len(filling) + 1
        m = len(filling[0]) + 1
        l = 0.75
        fig = plt.figure(figsize=(m * l, n * l))

        ax = fig.add_axes([0, 0, 1, 1])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        fill_cell(0, len(a) + 1, "black", ax)
        for i in range(len(a) + 1):
            fill_cell(0, i, "aquamarine", ax)
        for i in range(len(b) + 1):
            fill_cell(1 + i, len(a) + 1, "aquamarine", ax)

        for i in range(len(b)):
            ax.text(i + 2.5, len(a) + 1.5, b[i], color='black', ha='center', va='center', fontsize=20)
        for i in range(len(a)):
            ax.text(0.5, len(a) - 0.5 - i, a[i], color='black', ha='center', va='center', fontsize=20)

        for i in range(len(filling)):
            for j in range(len(filling[0])):
                ax.text(j + 1.5, len(a) + 2 - 1.5 - i, filling[i][j], color='black', ha='center', va='center',
                        fontsize=20)
                if i >= 1 and j >= 1:
                    if a[i - 1] == b[j - 1] and filling[i][j] != 0:
                        fill_cell(1 + j, len(a) - i, "aquamarine", ax)

        if bool:
            for i in range(len(x) - 1):
                ax.arrow(x[i], y[i], x[i + 1] - x[i], y[i + 1] - y[i], head_width=0.1, width=0.03, ec='black')

        for name, spine in ax.spines.items():
            spine.set_visible(False)
            spine.set_visible(False)

        for i in range(n + 1):
            ax.plot([0, m], [i, i], color='black')
        for i in range(m + 1):
            ax.plot([i, i], [0, n], color='black')
        plt.close(fig)
        return fig
    else:
        return None


a = input()
b = input()

filling = [0] * (len(a) + 1)
for i in range(len(a) + 1):
    filling[i] = ([0] * (len(b) + 1))

states = []


def fill(matrix, a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] == a[i]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            else:
                matrix[i + 1][j + 1] = max(matrix[i][j + 1], matrix[i + 1][j])
            states.append(draw_filling(filling, a, b, [], [], False))

    find_answer(matrix, a, b)


x = []
y = []
answer = []


def find_answer(matrix, a, b):
    i = len(a)
    j = len(b)
    for h in range(len(a) + len(b)):
        if matrix[i - 1][j] == matrix[i][j]:
            i -= 1
        elif matrix[i][j - 1] == matrix[i][j]:
            j -= 1
        else:
            answer.append(a[i - 1])
            x.append(1.5 + j)
            y.append(len(a) - i + 0.5)
            i -= 1
            j -= 1
            states.append(draw_filling(matrix, a, b, x, y, True))
        if i == 0 or j == 0:
            break


fill(filling, a, b)
animate_list(states, play=True, interval=400)
print("longest common subsequence is: " + ''.join(answer[::-1]))