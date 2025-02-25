# Animer le tracé

La cinquième étape consiste à animer le tracé. Nous allons utiliser une boucle `for` pour itérer sur une plage de valeurs de phi. Dans chaque itération, nous allons supprimer la collection de lignes précédente, générer de nouvelles données, tracer le nouveau maillage et mettre en pause brièvement avant de continuer.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
