# Personnaliser le graphique

Nous pouvons personnaliser le graphique en ajustant la ligne de base à l'aide du paramètre `bottom`. Nous pouvons également ajuster les propriétés de format du graphique à l'aide des paramètres `linefmt`, `markerfmt` et `basefmt`.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

Cela générera un graphique avec un format de ligne gris et des marqueurs en forme de losange. La ligne de base a également été ajustée à 1,1.
