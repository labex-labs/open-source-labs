# Créer l'animation

Nous allons maintenant créer l'animation à l'aide de la méthode ArtistAnimation. Nous passerons l'objet figure, la liste ims, l'intervalle entre les trames et le délai de répétition.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
