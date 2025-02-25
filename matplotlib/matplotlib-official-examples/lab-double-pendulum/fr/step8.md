# Créer l'animation

Nous allons maintenant créer l'animation en utilisant la fonction `FuncAnimation` de Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
