# Enregistrement du graphique

Une fois que nous avons créé un graphique, nous pouvons l'enregistrer dans un fichier.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Ici, nous utilisons la fonction `savefig` pour enregistrer notre graphique dans un fichier nommé `my_plot.png`.
