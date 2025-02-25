# Полный код

Вот полный код на Python для создания графика в форме шляпы.

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    Создает график в форме шляпы.

    Параметры
    ----------
    ax : matplotlib.axes.Axes
        оси (Axes), в которые будет нарисован график.
    xlabels : список строк
        имена категорий, которые будут отображаться по оси x.
    values : (M, N) массив подобного типа
        значения данных.
        Строки - это группы (len(group_labels) == M).
        Столбцы - это категории (len(xlabels) == N).
    group_labels : список строк
        метки групп, отображаемые в легенде.
    """

    def label_bars(heights, rects):
        """Прикрепляет текстовую метку сверху каждого столбца."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 точки вертикального смещения.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # расстояние между группами в форме шляпы
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# initialise labels and a numpy array make sure you have
# N labels of N number of values in the array
xlabels = ['I', 'II', 'III', 'IV', 'V']
playerA = np.array([5, 15, 22, 20, 25])
playerB = np.array([25, 32, 34, 30, 27])

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
