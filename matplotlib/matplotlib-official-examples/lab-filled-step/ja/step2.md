# ヒストグラム関数を定義する

ヒストグラムを段階的なパッチとして描画する関数を定義します。この関数は以下のパラメータを取ります。

- `ax`：描画するAxes
- `edges`：各ビンの左辺と最後のビンの右辺を与える長さn + 1の配列
- `values`：ビンのカウントまたは値の長さnの配列
- `bottoms`：floatまたは配列（オプション）、棒の下端の長さnの配列。Noneの場合、0が使用されます。
- `orientation`：文字列（オプション）、ヒストグラムの方向。'v'（既定値）は、棒が正のy方向に増加するようになっています。

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
