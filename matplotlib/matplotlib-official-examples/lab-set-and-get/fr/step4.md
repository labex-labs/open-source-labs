# Obtenir les propriétés

Nous pouvons utiliser la méthode `getp` pour obtenir les propriétés d'un objet. Nous pouvons l'utiliser pour interroger la valeur d'un seul attribut :

```python
plt.getp(line, 'linewidth')
```

Cela retournera la valeur de la propriété `linewidth` de l'objet `line`.

Nous pouvons également utiliser `getp` pour obtenir toutes les paires attribut/valeur d'un objet :

```python
plt.getp(line)
```

Cela retournera une longue liste de toutes les propriétés et de leurs valeurs.
