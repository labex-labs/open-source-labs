# Zeige das Bild und seinen Histogramm an

Als nächstes werden wir das Bild mit der `imshow`-Funktion von Matplotlib und dessen Histogramm mit `hist` anzeigen. Wir werden eine Figur mit zwei Teilplots erstellen, einen für das Bild und einen für das Histogramm.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
