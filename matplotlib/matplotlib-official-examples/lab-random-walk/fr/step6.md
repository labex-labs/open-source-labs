# Créer une animation

Nous créons une animation à l'aide de la classe `FuncAnimation` de `matplotlib.animation`. Nous passons l'objet figure, la fonction de mise à jour, le nombre total de trames (qui est égal au nombre de pas dans les mouvements aléatoires), la liste de tous les mouvements aléatoires et la liste de toutes les lignes en tant qu'arguments au constructeur `FuncAnimation`.

```python
# Création de l'objet Animation
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
