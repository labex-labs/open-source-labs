# Определяем функцию для гистограммы

Мы определим функцию для рисования гистограммы в виде ступенчатой области. Функция будет принимать следующие параметры:

- `ax`: оси для рисования
- `edges`: массив длиной n+1, задающий левые края каждого интервала и правый край последнего интервала
- `values`: массив длиной n с количеством элементов в каждом интервале или значениями
- `bottoms`: число или массив, необязательный, массив длиной n с нижними краями столбцов. Если None, используется ноль.
- `orientation`: строка, необязательная, ориентация гистограммы. 'v' (по умолчанию) означает, что столбцы возрастают в положительном направлении оси y.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Draw a histogram as a stepped patch.

    Parameters
    ----------
    ax : Axes
        The axes to plot to

    edges : array
        A length n+1 array giving the left edges of each bin and the
        right edge of the last bin.

    values : array
        A length n array of bin counts or values

    bottoms : float or array, optional
        A length n array of the bottom of the bars.  If None, zero is used.

    orientation : {'v', 'h'}
       Orientation of the histogram.  'v' (default) has
       the bars increasing in the positive y-direction.

    **kwargs
        Extra keyword arguments are passed through to `.fill_between`.

    Returns
    -------
    ret : PolyCollection
        Artist added to the Axes
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
