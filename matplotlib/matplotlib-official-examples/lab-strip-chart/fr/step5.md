# Configuration du graphique

Nous créons un nouvel objet figure et un nouvel objet axe, puis nous initialisons la classe Scope. Ensuite, nous passons les fonctions de mise à jour et d'émission à la méthode `FuncAnimation` pour créer l'animation.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
