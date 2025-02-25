# Définition de la fonction de tracé

Maintenant, vous devez définir la fonction `plot_figure()` qui configurera et tracera la figure de démonstration avec un style donné. Cette fonction appellera chacune des fonctions de tracé définies dans l'Étape 2.

```python
def plot_figure(style_label=""):
    """Configure et trace la figure de démonstration avec un style donné."""
    # Utilisez une instance dédiée de RandomState pour tracer les mêmes valeurs "aléatoires"
    # sur les différentes figures.
    prng = np.random.RandomState(96917002)

    fig, axs = plt.subplots(ncols=6, nrows=1, num=style_label,
                            figsize=(14.8, 2.8), layout='constrained')

    # Crée un supertitre, dans le même style pour toutes les sous-figures,
    # sauf celles avec des fonds foncés, qui obtiennent une couleur plus claire :
    background_color = mcolors.rgb_to_hsv(
        mcolors.to_rgb(plt.rcParams['figure.facecolor']))[2]
    if background_color < 0.5:
        title_color = [0.8, 0.8, 1]
    else:
        title_color = np.array([19, 6, 84]) / 256
    fig.suptitle(style_label, x=0.01, ha='left', color=title_color,
                 fontsize=14, fontfamily='DejaVu Sans', fontweight='normal')

    plot_scatter(axs[0], prng)
    plot_image_and_patch(axs[1], prng)
    plot_bar_graphs(axs[2], prng)
    plot_colored_lines(axs[3])
    plot_histograms(axs[4], prng)
    plot_colored_circles(axs[5], prng)

    # ajoute un séparateur
    rec = Rectangle((1 + 0.025, -2), 0.05, 16,
                    clip_on=False, color='gray')

    axs[4].add_artist(rec)
```
