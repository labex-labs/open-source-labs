# Créer une animation

Maintenant que nous avons défini la classe `UpdateDist`, nous pouvons créer l'animation en utilisant la classe `FuncAnimation` de Matplotlib. Nous créons un objet figure et un objet axe et passons l'objet axe à la classe `UpdateDist` pour créer une nouvelle instance de la classe.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

La classe `FuncAnimation` prend plusieurs arguments :

- `fig` : l'objet figure
- `ud` : l'instance de `UpdateDist`
- `frames` : le nombre d'images à animer
- `interval` : le temps entre les images en millisecondes
- `blit` : indique si seulement les parties du tracé qui ont changé doivent être mises à jour
