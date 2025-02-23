# Créez l'animation

Nous utiliserons une boucle `for` pour itérer sur chaque trame de l'animation. Dans chaque itération, nous allons effacer l'axe, tracer la trame actuelle, définir le titre et mettre en pause pendant un court laps de temps pour permettre l'affichage de l'animation.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"trame {i}")
    plt.pause(0.1)
```
