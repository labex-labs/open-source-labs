# Definir a função de plotagem

Agora, você precisa definir a função `plot_figure()` que configurará e plotará a figura de demonstração com um determinado estilo. Esta função chamará cada uma das funções de plotagem definidas no Passo 2.

```python
def plot_figure(style_label=""):
    """Configura e plota a figura de demonstração com um determinado estilo."""
    # Use uma instância RandomState dedicada para desenhar os mesmos valores "aleatórios"
    # em todas as diferentes figuras.
    prng = np.random.RandomState(96917002)

    fig, axs = plt.subplots(ncols=6, nrows=1, num=style_label,
                            figsize=(14.8, 2.8), layout='constrained')

    # faça um suptitle, no mesmo estilo para todas as subfiguras,
    # exceto aquelas com fundos escuros, que recebem uma cor mais clara:
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

    # adiciona divisor
    rec = Rectangle((1 + 0.025, -2), 0.05, 16,
                    clip_on=False, color='gray')

    axs[4].add_artist(rec)
```
