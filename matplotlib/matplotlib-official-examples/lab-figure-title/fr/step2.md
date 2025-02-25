# Ajoutez des étiquettes x et y globales à une figure

Ensuite, nous allons ajouter des étiquettes x et y globales à une figure montrant les prix d'actions relatifs de différentes entreprises au fil du temps. Nous utiliserons la fonction `np.genfromtxt()` pour lire un fichier CSV contenant des données sur les prix d'actions puis tracer les données pour chaque entreprise à l'aide de sous-graphiques. Nous utiliserons les méthodes `fig.supxlabel()` et `fig.supylabel()` pour ajouter des étiquettes x et y globales à la figure.

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
fig.supxlabel('Année')
fig.supylabel('Prix d\'action par rapport au maximum')

plt.show()
```
