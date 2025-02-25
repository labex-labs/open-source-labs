# Créer un diagramme à violon par défaut

Ensuite, nous allons créer un diagramme à violon par défaut à l'aide de la fonction `violinplot` de Matplotlib. Cela servira de référence pour la comparaison lorsque nous personnaliserons le graphique dans les étapes suivantes.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
