# Matplotlibのインポートとグラフの設定

まず、Matplotlibライブラリをインポートしてグラフを設定します。1つのy軸と1つのx軸を持つ空のグラフを作成します。また、軸を設定して下側の目盛り線のみを表示し、目盛りの位置を設定し、目盛りの長さを定義します。

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # define tick positions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Tick Formatters")
```

# Matplotlibをインポートしてグラフを設定する

まず、Matplotlibライブラリをインポートしてグラフを設定します。1つのy軸と1つのx軸を持つ空のグラフを作成します。また、軸を設定して下側の目盛り線のみを表示し、目盛りの位置を設定し、目盛りの長さを定義します。

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """この例でのAxesの共通パラメータを設定します。"""
    # 下側の目盛り線のみを表示
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # 目盛りの位置を定義
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Tick Formatters")
```
