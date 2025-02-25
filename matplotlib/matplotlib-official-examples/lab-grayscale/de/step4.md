# Definieren der Funktion für das Bild- und Patch-Beispiel

Wir definieren die Funktion `image_and_patch_example`, die ein Achsenobjekt als Eingabe nimmt, ein zufälliges Bild darstellt und einem Plot einen Patch hinzufügt.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
