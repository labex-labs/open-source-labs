# Personnaliser l'affichage des différents éléments

Nous pouvons personnaliser l'affichage des différents éléments du diagramme en boîte en utilisant divers paramètres dans la fonction `bxp()`. Dans cet exemple, nous montrons comment personnaliser la boîte, la médiane, les points aberrants, le point moyen et la ligne moyenne.

```python
# Personnaliser l'affichage des différents éléments
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.bxp(stats, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, meanline=True, showmeans=True)
plt.show()
```
