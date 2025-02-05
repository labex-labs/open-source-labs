# 为图形添加全局 x 轴和 y 轴标签

接下来，我们将为一个展示不同公司随时间变化的相对股价的图形添加全局 x 轴和 y 轴标签。我们将使用 `np.genfromtxt()` 函数读取一个包含股价数据的 CSV 文件，然后使用子图绘制每个公司的数据。我们将使用 `fig.supxlabel()` 和 `fig.supylabel()` 方法为图形添加全局 x 轴和 y 轴标签。

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
