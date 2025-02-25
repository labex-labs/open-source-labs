# グラフにグローバルな x 軸と y 軸のラベルを追加する

次に、異なる会社の相対株価を時間とともに示すグラフにグローバルな x 軸と y 軸のラベルを追加します。株価データを含む CSV ファイルを読み込むために `np.genfromtxt()` 関数を使用し、その後、サブプロットを使用して各会社のデータをプロットします。グラフにグローバルな x 軸と y 軸のラベルを追加するために、`fig.supxlabel()` メソッドと `fig.supylabel()` メソッドを使用します。

```python
from matplotlib.cbook import get_sample_data

with get_sample_data('Stocks.csv') as file:
    stocks = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex=True, sharey=True)
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = stocks[column_name]
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Year')
fig.supylabel('Stock price relative to max')

plt.show()
```
