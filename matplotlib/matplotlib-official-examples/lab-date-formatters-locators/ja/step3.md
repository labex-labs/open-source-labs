# グラフの描画

これで、グラフを作成することができます。位置付け関数とフォーマッタをそれぞれ別々に示すために、2 つのサブプロットを作成します。各位置付け関数とフォーマッタについて、それが X 軸にどのような影響を与えるかを示すグラフを描画します。これを行うために `plot_axis` 関数を使用します。この関数は、各軸の共通パラメータ、たとえばスパイン、目盛りパラメータ、および制限を設定します。また、X 軸の位置付け関数とフォーマッタも設定します。

```python
def plot_axis(ax, locator=None, xmax='2002-02-01', fmt=None, formatter=None):
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(np.datetime64('2000-02-01'), np.datetime64(xmax))
    if locator:
        ax.xaxis.set_major_locator(eval(locator))
        ax.xaxis.set_major_formatter(DateFormatter(fmt))
    else:
        ax.xaxis.set_major_formatter(eval(formatter))
    ax.text(0.0, 0.2, locator or formatter, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, axs = plt.subplots(len(locators), 1, figsize=(8, len(locators) *.8),
                        layout='constrained')
fig.suptitle('Date Locators')
for ax, (locator, xmax, fmt) in zip(axs, locators):
    plot_axis(ax, locator, xmax, fmt)

fig, axs = plt.subplots(len(formatters), 1, figsize=(8, len(formatters) *.8),
                        layout='constrained')
fig.suptitle('Date Formatters')
for ax, fmt in zip(axs, formatters):
    plot_axis(ax, formatter=fmt)
```
