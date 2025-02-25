# Definir la función de histograma

Definiremos una función para dibujar un histograma como un parche escalonado. La función tomará los siguientes parámetros:

- `ax`: los Ejes en los que se dibujará
- `edges`: una matriz de longitud n+1 que da los bordes izquierdos de cada intervalo y el borde derecho del último intervalo
- `values`: una matriz de longitud n de conteos o valores de intervalos
- `bottoms`: un flotante o matriz, opcional, una matriz de longitud n de la base de las barras. Si es None, se utiliza cero.
- `orientation`: una cadena, opcional, la orientación del histograma. 'v' (por defecto) hace que las barras crezcan en la dirección y positiva.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Dibuja un histograma como un parche escalonado.

    Parámetros
    ----------
    ax : Ejes
        Los ejes en los que se dibujará

    edges : matriz
        Una matriz de longitud n+1 que da los bordes izquierdos de cada intervalo y el
        borde derecho del último intervalo.

    values : matriz
        Una matriz de longitud n de conteos o valores de intervalos

    bottoms : flotante o matriz, opcional
        Una matriz de longitud n de la base de las barras.  Si es None, se utiliza cero.

    orientation : {'v', 'h'}
       Orientación del histograma.  'v' (por defecto) hace que
       las barras crezcan en la dirección y positiva.

    **kwargs
        Argumentos de palabras clave adicionales se transmiten a `.fill_between`.

    Devuelve
    -------
    ret : PolyCollection
        Artista agregado a los Ejes
    """
    if orientation not in 'hv':
        raise ValueError(f"orientation must be in {{'h', 'v'}} not {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1!= len(values):
        raise ValueError(f'Must provide one more bin edge than value not: {len(edges)=} {len(values)=}')

    if bottoms is None:
        bottoms = 0
    bottoms = np.broadcast_to(bottoms, values.shape)

    values = np.append(values, values[-1])
    bottoms = np.append(bottoms, bottoms[-1])
    if orientation == 'h':
        return ax.fill_betweenx(edges, values, bottoms, **kwargs)
    elif orientation == 'v':
        return ax.fill_between(edges, values, bottoms, **kwargs)
    else:
        raise AssertionError("you should never be here")
```
