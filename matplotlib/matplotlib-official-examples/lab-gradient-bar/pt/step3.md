# Definir a função de imagem gradiente

Precisamos definir uma função que criará uma imagem gradiente com base em um mapa de cores (colormap). Esta função receberá um objeto de eixos (axes), a direção do gradiente e a faixa do mapa de cores a ser usado. A função então gerará a imagem gradiente e a retornará.

```python
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Desenha uma imagem gradiente com base em um mapa de cores.

    Parâmetros
    ----------
    ax : Axes
        Os eixos para desenhar.
    direction : float
        A direção do gradiente. Este é um número no intervalo
        de 0 (=vertical) a 1 (=horizontal).
    cmap_range : float, float
        A fração (cmin, cmax) do mapa de cores que deve ser
        usada para o gradiente, onde o mapa de cores completo é (0, 1).
    **kwargs
        Outros parâmetros são passados para `.Axes.imshow()`.
        Em particular, *cmap*, *extent* e *transform* podem ser úteis.
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im
```
