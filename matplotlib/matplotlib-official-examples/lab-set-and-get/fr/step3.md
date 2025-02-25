# Définition de propriétés

L'interface pyplot nous permet de définir et d'obtenir les propriétés d'objets pour visualiser des données. Nous pouvons utiliser la méthode `setp` pour définir les propriétés d'un objet. Par exemple, pour définir le style de ligne d'une ligne en tirets rompus, nous utilisons le code suivant :

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

Si nous voulons savoir les types valides d'arguments, nous pouvons fournir le nom de la propriété que nous voulons définir sans valeur :

```python
plt.setp(line, 'linestyle')
```

Cela retournera la sortie suivante :

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq),...}
```

Si nous voulons voir toutes les propriétés qui peuvent être définies, et leurs valeurs possibles, nous pouvons utiliser le code suivant :

```python
plt.setp(line)
```

Cela retournera une longue liste de propriétés et de leurs valeurs possibles.
