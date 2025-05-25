# Definir a Função `confidence_ellipse`

Em seguida, definimos a função `confidence_ellipse` que receberá as coordenadas x e y do conjunto de dados, o objeto de eixos para desenhar a elipse e o número de desvios padrão. Ela retorna um objeto patch do Matplotlib representando a elipse.

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Cria um gráfico da elipse de confiança da covariância de *x* e *y*.

    Parâmetros
    ----------
    x, y : array-like, shape (n, )
        Dados de entrada.

    ax : matplotlib.axes.Axes
        O objeto de eixos para desenhar a elipse.

    n_std : float
        O número de desvios padrão para determinar os raios da elipse.

    **kwargs
        Encaminhado para `~matplotlib.patches.Ellipse`

    Retorna
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
