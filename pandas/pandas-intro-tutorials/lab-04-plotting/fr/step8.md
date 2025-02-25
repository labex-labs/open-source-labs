# Personnaliser et enregistrer le graphique

Nous pouvons personnaliser davantage le graphique en utilisant les options de personnalisation de Matplotlib. Nous pouvons également enregistrer le graphique dans un fichier.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
