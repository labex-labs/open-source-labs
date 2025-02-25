# Definir las funciones de trazado

A continuación, debes definir las funciones de trazado que se utilizarán para crear los gráficos de ejemplo. En este paso, definirás las siguientes funciones de trazado:

- `plot_scatter()`: crea un diagrama de dispersión
- `plot_colored_lines()`: traza líneas con colores siguiendo el ciclo de colores de estilo
- `plot_bar_graphs()`: crea un gráfico de barras
- `plot_colored_circles()`: traza parches circulares
- `plot_image_and_patch()`: traza una imagen con un parche circular
- `plot_histograms()`: crea histogramas

```python
def plot_scatter(ax, prng, nb_samples=100):
    """Diagrama de dispersión."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1.,'s')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('Etiqueta de X')
    ax.set_title('Título de los ejes')
    return ax


def plot_colored_lines(ax):
    """Traza líneas con colores siguiendo el ciclo de colores de estilo."""
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
    """Traza dos gráficos de barras lado a lado, con letras como etiquetas de marcas de tiempo en x."""
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    Traza parches circulares.

    NB: dibuja una cantidad fija de muestras, en lugar de utilizar la longitud
    del ciclo de colores, porque diferentes estilos pueden tener diferentes
    números de colores.
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # Agrega un título para habilitar la cuadrícula
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # para trazar círculos como círculos
    return ax


def plot_image_and_patch(ax, prng, size=(20, 20)):
    """Traza una imagen con valores aleatorios y superpone un parche circular."""
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='parche')
    ax.add_patch(c)
    # Elimina las marcas de tiempo
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histograms(ax, prng, nb_samples=10000):
    """Traza 4 histogramas y una anotación de texto."""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # Agrega una pequeña anotación.
    ax.annotate('Anotación', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    return ax
```
