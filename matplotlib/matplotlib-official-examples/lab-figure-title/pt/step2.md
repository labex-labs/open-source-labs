# Adicionar rótulos globais x e y a uma figura

Em seguida, adicionaremos rótulos globais x e y a uma figura mostrando os preços relativos das ações de diferentes empresas ao longo do tempo. Usaremos a função `np.genfromtxt()` para ler um arquivo CSV contendo dados de preços de ações e, em seguida, plotaremos os dados para cada empresa usando subplots. Usaremos os métodos `fig.supxlabel()` e `fig.supylabel()` para adicionar rótulos globais x e y à figura.

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
