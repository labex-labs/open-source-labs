# Création de l'animation

La dernière étape est de créer l'animation. Nous le faisons à l'aide de la fonction `FuncAnimation` du module `animation`. Cette fonction prend plusieurs arguments, y compris l'objet figure, la fonction qui mettra à jour le graphique et le nombre d'images à utiliser.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
