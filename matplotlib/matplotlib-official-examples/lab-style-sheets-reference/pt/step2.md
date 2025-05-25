# Definir as funções de plotagem

Em seguida, você precisa definir as funções de plotagem que serão usadas para criar os gráficos de exemplo. Nesta etapa, você definirá as seguintes funções de plotagem:

- `plot_scatter()`: cria um gráfico de dispersão (scatter plot)
- `plot_colored_lines()`: plota linhas com cores seguindo o ciclo de cores do estilo
- `plot_bar_graphs()`: cria um gráfico de barras
- `plot_colored_circles()`: plota círculos
- `plot_image_and_patch()`: plota uma imagem com um patch circular
- `plot_histograms()`: cria histogramas

```python
def plot_scatter(ax, prng, nb_samples=100):
    """Gráfico de dispersão (Scatter plot)."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X-label')
    ax.set_title('Título dos eixos')
    return ax


def plot_colored_lines(ax):
    """Plota linhas com cores seguindo o ciclo de cores do estilo."""
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
    """Plota dois gráficos de barras lado a lado, com letras como rótulos do eixo x."""
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    Plota círculos.

    NB: desenha uma quantidade fixa de amostras, em vez de usar o comprimento do
    ciclo de cores, porque diferentes estilos podem ter diferentes números
    de cores.
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # Adiciona título para habilitar a grade
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # para plotar círculos como círculos
    return ax


def plot_image_and_patch(ax, prng, size=(20, 20)):
    """Plota uma imagem com valores aleatórios e sobrepõe um patch circular."""
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histograms(ax, prng, nb_samples=10000):
    """Plota 4 histogramas e uma anotação de texto."""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # Adiciona uma pequena anotação.
    ax.annotate('Anotação', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    return ax
```
