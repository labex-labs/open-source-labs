# Definir la función `confidence_ellipse`

A continuación, definimos la función `confidence_ellipse` que tomará las coordenadas x e y del conjunto de datos, el objeto de ejes en el que se dibujará la elipse y el número de desviaciones estándar. Devuelve un objeto de parche (patch) de Matplotlib que representa la elipse.

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Crea un gráfico de la elipse de confianza de la covarianza de *x* e *y*.

    Parámetros
    ----------
    x, y : array-like, shape (n, )
        Datos de entrada.

    ax : matplotlib.axes.Axes
        El objeto de ejes en el que se dibujará la elipse.

    n_std : float
        El número de desviaciones estándar para determinar los radios de la elipse.

    **kwargs
        Se pasan a `~matplotlib.patches.Ellipse`

    Devuelve
    -------
    matplotlib.patches.Ellipse
    """
    if x.size!= y.size:
        raise ValueError("x y y deben tener el mismo tamaño")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Usando un caso especial para obtener los eigenvalores de este
    # conjunto de datos bidimensional.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculando la desviación estándar de x a partir
    # de la raíz cuadrada de la varianza y multiplicando
    # por el número dado de desviaciones estándar.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculando la desviación estándar de y...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
       .rotate_deg(45) \
       .scale(scale_x, scale_y) \
       .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
