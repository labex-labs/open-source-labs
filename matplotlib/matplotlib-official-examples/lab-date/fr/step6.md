# Formater les étiquettes d'échelle à l'aide du formateur concise

Nous allons formater les étiquettes d'échelle sur le deuxième sous-graphique à l'aide du formateur concise.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
