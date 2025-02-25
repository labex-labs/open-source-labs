# カラーサイクルの例を示す関数の定義

`color_cycle_example` という関数を定義します。この関数は軸オブジェクトを入力として受け取り、カラーサイクル内の各色に対して正弦波を描画します。カラーサイクルは `rcParams` によって定義されます。

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
