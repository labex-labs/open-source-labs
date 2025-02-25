# Masquage des points de données et création d'un graphique en nuage de points

Nous masquons les points de données en fonction de leur distance par rapport à l'origine. Les points de données dont la distance est inférieure à `r0` sont masqués dans `area1`, et ceux dont la distance est supérieure ou égale à `r0` sont masqués dans `area2`. Nous créons ensuite un graphique en nuage de points des points de données masqués avec `marker='^'` et `marker='o'` pour `area1` et `area2` respectivement.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
