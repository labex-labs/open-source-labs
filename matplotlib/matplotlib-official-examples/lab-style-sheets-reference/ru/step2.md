# Определить функции для построения графиков

Далее вам нужно определить функции для построения графиков, которые будут использоваться для создания примерных графиков. В этом шаге вы определите следующие функции для построения графиков:

- `plot_scatter()`: создает диаграмму рассеяния
- `plot_colored_lines()`: строит линии с цветами в соответствии с циклом стилей цветов
- `plot_bar_graphs()`: создает столбчатую диаграмму
- `plot_colored_circles()`: рисует круговые участки
- `plot_image_and_patch()`: рисует изображение с круговым участком
- `plot_histograms()`: создает гистограммы

```python
def plot_scatter(ax, prng, nb_samples=100):
    """Диаграмма рассеяния."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1.,'s')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X-метка')
    ax.set_title('Заголовок осей')
    return ax


def plot_colored_lines(ax):
    """Строит линии с цветами в соответствии с циклом стилей цветов."""
    t = np.linspace(-10, 10, 100)

    def sigmoid(t, t0):
        return 1 / (1 + np.exp(-(t - t0)))

    nb_colors = len(plt.rcParams['axes.prop_cycle'])
    shifts = np.linspace(-5, 5, nb_colors)
    amplitudes = np.linspace(1, 1.5, nb_colors)
    for t0, a in zip(shifts, amplitudes):
        ax.plot(t, a * sigmoid(t, t0), '-')
    ax.set_xlim(-10, 10)
    return ax


def plot_bar_graphs(ax, prng, min_value=5, max_value=25, nb_samples=5):
    """Строит две столбчатые диаграммы рядом, с буквами в качестве меток по оси x."""
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    Рисует круговые участки.

    NB: рисует фиксированное количество образцов, а не использует длину
    цикла цветов, так как разные стили могут иметь разные количества
    цветов.
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # Добавить заголовок для включения сетки
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # чтобы рисовать круги как круги
    return ax


def plot_image_and_patch(ax, prng, size=(20, 20)):
    """Рисует изображение со случайными значениями и накладывает на него круговой участок."""
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
    # Удалить деления
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histograms(ax, prng, nb_samples=10000):
    """Строит 4 гистограммы и текстовую аннотацию."""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # Добавить небольшую аннотацию.
    ax.annotate('Аннотация', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    return ax
```
