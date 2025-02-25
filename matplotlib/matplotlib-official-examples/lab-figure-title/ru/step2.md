# Добавьте глобальные подписи по осям x и y к графику

Далее мы добавим глобальные подписи по осям x и y к графику, показывающему относительные цены акций различных компаний в течение времени. Мы будем использовать функцию `np.genfromtxt()` для чтения CSV-файла, содержащего данные о ценах на акции, и затем построить данные для каждой компании с использованием подграфиков. Мы будем использовать методы `fig.supxlabel()` и `fig.supylabel()` для добавления глобальных подписей по осям x и y к графику.

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
fig.supxlabel('Год')
fig.supylabel('Цена акции относительно максимума')

plt.show()
```
