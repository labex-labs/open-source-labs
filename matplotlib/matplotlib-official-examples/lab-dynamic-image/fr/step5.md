# Créer les trames d'animation

Nous allons maintenant créer les trames pour l'animation. Nous utiliserons une boucle for pour générer 60 trames. Dans chaque itération de la boucle, nous mettrons à jour les données x et y puis créerons un nouvel objet image à l'aide de la méthode imshow. Nous ajouterons ensuite l'objet image à la liste ims.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
