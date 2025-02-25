# Agrega etiquetas globales en los ejes x e y a una figura

A continuación, agregaremos etiquetas globales en los ejes x e y a una figura que muestra los precios relativos de acciones de diferentes empresas a lo largo del tiempo. Utilizaremos la función `np.genfromtxt()` para leer un archivo CSV que contiene datos de precios de acciones y luego graficaremos los datos de cada empresa utilizando subgráficos. Utilizaremos los métodos `fig.supxlabel()` y `fig.supylabel()` para agregar etiquetas globales en los ejes x e y a la figura.

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
fig.supxlabel('Año')
fig.supylabel('Precio de la acción relativo al máximo')

plt.show()
```
