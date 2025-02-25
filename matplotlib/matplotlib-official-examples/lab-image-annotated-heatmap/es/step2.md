# Estilo de código de la función auxiliar

Crearemos una función que tome los datos y las etiquetas de filas y columnas como entrada y permita argumentos que se usen para personalizar la gráfica. Apagaremos las espinas de los ejes circundantes y crearemos una cuadrícula de líneas blancas para separar las celdas. Aquí, también queremos crear una barra de colores y posicionar las etiquetas encima del mapa de calor en lugar de debajo de él. Las anotaciones tendrán diferentes colores según un umbral para un mejor contraste con el color de los píxeles.

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    Crea un mapa de calor a partir de una matriz de numpy y dos listas de etiquetas.

    Parámetros
    ----------
    data
        Una matriz bidimensional de numpy de forma (M, N).
    row_labels
        Una lista o matriz de longitud M con las etiquetas de las filas.
    col_labels
        Una lista o matriz de longitud N con las etiquetas de las columnas.
    ax
        Una instancia de `matplotlib.axes.Axes` a la que se traza el mapa de calor. Si no se proporciona, se utiliza el eje actual o se crea uno nuevo. Opcional.
    cbar_kw
        Un diccionario con argumentos para `matplotlib.Figure.colorbar`. Opcional.
    cbarlabel
        La etiqueta para la barra de colores. Opcional.
    **kwargs
        Todos los demás argumentos se transmiten a `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Dibuja el mapa de calor
    im = ax.imshow(data, **kwargs)

    # Crea la barra de colores
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Muestra todas las marcas de división y las etiqueta con las respectivas entradas de la lista.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Hace que las etiquetas de los ejes horizontales aparezcan en la parte superior.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Rota las etiquetas de las marcas de división y establece su alineación.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Apaga las espinas y crea una cuadrícula blanca.
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    Una función para anotar un mapa de calor.

    Parámetros
    ----------
    im
        La AxesImage que se va a etiquetar.
    data
        Datos utilizados para la anotación. Si es None, se utilizan los datos de la imagen. Opcional.
    valfmt
        El formato de las anotaciones dentro del mapa de calor. Esto debe utilizar el método de formato de cadenas, por ejemplo, "$ {x:.2f}", o ser un `matplotlib.ticker.Formatter`. Opcional.
    textcolors
        Un par de colores. El primero se utiliza para los valores por debajo de un umbral, el segundo para aquellos por encima. Opcional.
    threshold
        Valor en unidades de datos según el cual se aplican los colores de textcolors. Si es None (el valor predeterminado), se utiliza el centro de la paleta de colores como separación. Opcional.
    **kwargs
        Todos los demás argumentos se transmiten a cada llamada a `text` utilizada para crear las etiquetas de texto.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normaliza el umbral al rango de colores de la imagen.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Establece la alineación predeterminada en el centro, pero permite que se reescriba por textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Obtiene el formateador en caso de que se proporcione una cadena
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Itera sobre los datos y crea un `Text` para cada "pixel".
    # Cambia el color del texto según los datos.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
