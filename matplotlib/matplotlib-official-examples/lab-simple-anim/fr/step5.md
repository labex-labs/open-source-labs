# Créer l'objet d'animation

Maintenant, nous pouvons créer l'objet d'animation à l'aide de la fonction `FuncAnimation()`. Nous passerons l'objet figure, la fonction d'animation, l'intervalle de mise à jour et le nombre d'images à enregistrer.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
