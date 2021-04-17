import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import random
from interactive_visualization.animation_utils import animate_list
from IPython.display import Code

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
names = [name for hsv, name in by_hsv if
         name not in {'black', 'k', 'w', 'white', 'crimson', 'royalblue', 'limegreen', 'yellow', 'orange'}]
import random

random.shuffle(names)
names = ['crimson', 'royalblue', 'limegreen', 'yellow', 'orange', *names]
names.append('red')
names.append('white')
names.append('black')


def fill_cell(i, j, color, ax):
    ax.fill([i, i, i + 1, i + 1, i], [j, j + 1, j + 1, j, j], text="a")


def draw_filling(filling, a, b):
    if filling is not None:
        n = len(filling)
        m = len(filling[0])
        x = 0.75
        fig = plt.figure(figsize=(m * x, n * x))

        ax = fig.add_axes([0, 0, 1, 1])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(a, b, "a", color='green', ha='center', va='center')
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


def shit(filling):
    a = 0
    b = 0
    while True:
        if a >= 10:
            break
        else:
            states.append(draw_filling(filling, a, b))
            a += 1
            b += 1


for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        print(filling[i][j], end=" ")
    print()
shit(filling)
animate_list(states, play=True, interval=400)
draw_filling(filling)