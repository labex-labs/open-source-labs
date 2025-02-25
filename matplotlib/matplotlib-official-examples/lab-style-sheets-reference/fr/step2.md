# Définition des fonctions de tracé

Ensuite, vous devez définir les fonctions de tracé qui seront utilisées pour créer les graphiques d'exemple. Dans cette étape, vous définirez les fonctions de tracé suivantes :

- `plot_scatter()` : crée un graphique de dispersion
- `plot_colored_lines()` : trace des lignes avec des couleurs suivant le cycle de couleurs du style
- `plot_bar_graphs()` : crée un diagramme en barres
- `plot_colored_circles()` : trace des patches circulaires
- `plot_image_and_patch()` : trace une image avec une patch circulaire
- `plot_histograms()` : crée des histogrammes

```python
def plot_scatter(ax, prng, nb_samples=100):
    """Graphique de dispersion."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1.,'s')]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('Étiquette de l\'axe X')
    ax.set_title('Titre des axes')
    return ax


def plot_colored_lines(ax):
    """Trace des lignes avec des couleurs suivant le cycle de couleurs du style."""
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
    """Trace deux diagrammes en barres côte à côte, avec des lettres comme étiquettes d'axe x."""
    x = np.arange(nb_samples)
    ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.25
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
    return ax


def plot_colored_circles(ax, prng, nb_samples=15):
    """
    Trace des patches circulaires.

    NB : trace un nombre fixe d'échantillons, plutôt que d'utiliser la longueur
    du cycle de couleurs, car différents styles peuvent avoir un nombre différent
    de couleurs.
    """
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(prng.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))
    ax.grid(visible=True)

    # Ajoute un titre pour activer la grille
    plt.title('ax.grid(True)', family='monospace', fontsize='small')

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # pour tracer les cercles comme des cercles
    return ax


def plot_image_and_patch(ax, prng, size=(20, 20)):
    """Trace une image avec des valeurs aléatoires et superpose une patch circulaire."""
    values = prng.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
    # Supprime les étiquettes d'axe
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histograms(ax, prng, nb_samples=10000):
    """Trace 4 histogrammes et une annotation de texte."""
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = prng.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    # Ajoute une petite annotation.
    ax.annotate('Annotation', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    return ax
```
