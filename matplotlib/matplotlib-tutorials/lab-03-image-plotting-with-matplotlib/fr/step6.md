# Schémas d'interpolation d'un tableau

Lors du redimensionnement d'une image, il est nécessaire d'interpoler les valeurs des pixels pour combler l'espace manquant. Différents schémas d'interpolation peuvent être utilisés pour déterminer la valeur d'un pixel en fonction de ses pixels environnants. Matplotlib propose différentes options d'interpolation, telles que "nearest", "bilinear" et "bicubic".

```python
plt.imshow(img, interpolation="bilinear")
```
