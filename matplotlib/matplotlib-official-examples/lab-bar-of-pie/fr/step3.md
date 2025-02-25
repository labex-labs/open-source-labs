# Créez le graphique camembert

Maintenant, nous pouvons créer le graphique camembert. Nous commençons par définir les objets figure et axe :

```python
# créez la figure et attribuez les objets axe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

Ensuite, nous définissons les paramètres du graphique camembert et le traçons :

```python
# faites une rotation pour que la première tranche soit divisée par l'axe des x
angle = -180 * rapports_généraux[0]
tranchées, *_ = ax1.pie(rapports_généraux, autopct='%1.1f%%', startangle=angle,
                     labels=étiquettes, explode=éclatement)
```
