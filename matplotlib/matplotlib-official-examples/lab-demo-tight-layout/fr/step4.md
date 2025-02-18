# Création de plusieurs graphiques

Nous pouvons également créer plusieurs graphiques dans la même figure.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Ici, nous utilisons la fonction `subplot` pour créer deux graphiques côte à côte dans la même figure. Nous passons trois arguments à `subplot` : le nombre de lignes, le nombre de colonnes et le numéro du graphique. Ensuite, nous créons un graphique dans chaque sous-graphique.
