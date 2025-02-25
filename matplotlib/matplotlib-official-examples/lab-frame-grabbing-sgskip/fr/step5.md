# Capturer les images et enregistrer dans un fichier

Nous effectuons une boucle de 100 itérations et générons des nombres aléatoires pour les coordonnées x et y. Nous mettons à jour les données du tracé de ligne et capturons l'image à l'aide de l'écrivain. Enfin, nous enregistrons les images dans un fichier.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
