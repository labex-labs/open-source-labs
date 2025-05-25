# Definir a função do histograma

Definiremos uma função para desenhar um histograma como um patch em degraus. A função receberá os seguintes parâmetros:

- `ax`: os Axes (eixos) para plotar
- `edges`: um array de comprimento n+1 que fornece as bordas esquerdas de cada bin e a borda direita do último bin
- `values`: um array de comprimento n de contagens ou valores de bin
- `bottoms`: um float ou array, opcional, um array de comprimento n da base das barras. Se None, zero é usado.
- `orientation`: uma string, opcional, a orientação do histograma. 'v' (padrão) tem as barras aumentando na direção y positiva.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Desenha um histograma como um patch em degraus.

    Parâmetros
    ----------
    ax : Axes
        Os eixos para plotar

    edges : array
        Um array de comprimento n+1 que fornece as bordas esquerdas de cada bin e a
        borda direita do último bin.

    values : array
        Um array de comprimento n de contagens ou valores de bin

    bottoms : float ou array, opcional
        Um array de comprimento n da base das barras. Se None, zero é usado.

    orientation : {'v', 'h'}
       Orientação do histograma. 'v' (padrão) tem
       as barras aumentando na direção y positiva.

    **kwargs
        Argumentos de palavra-chave extras são passados para `.fill_between`.

    Retorna
    -------
    ret : PolyCollection
        Artista adicionado aos Axes
    """
    if orientation not in 'hv':
        raise ValueError(f"orientation must be in {{'h', 'v'}} not {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1 != len(values):
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
