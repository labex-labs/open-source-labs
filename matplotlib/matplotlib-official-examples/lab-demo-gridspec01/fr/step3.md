# Définir des sous-graphiques à l'aide de subplot2grid

Pour définir des sous-graphiques à l'aide de `subplot2grid`, nous devons tout d'abord spécifier la taille de la grille en utilisant un tuple avec le nombre souhaité de lignes et de colonnes. Nous devons également spécifier l'emplacement du sous-graphique dans la grille en utilisant un autre tuple.

Par exemple, pour créer une grille 3x3 avec un sous-graphique qui couvre toute la première ligne et les trois colonnes, nous utilisons le code suivant :

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```

Pour créer un sous-graphique qui couvre la deuxième ligne et les deux premières colonnes, nous utilisons :

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

Pour créer un sous-graphique qui couvre les deux dernières lignes et la dernière colonne, nous utilisons :

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```

Pour créer un sous-graphique dans la dernière ligne et la première colonne, nous utilisons :

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```

Pour créer un sous-graphique dans la dernière ligne et la deuxième colonne, nous utilisons :

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
