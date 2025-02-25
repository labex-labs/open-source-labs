# Plotten des Histogramms der MRT-Intensität

Als nächstes werden wir das Histogramm der MRT-Intensität mit der `hist()`-Funktion plotten. Wir werden die Intensitätswerte auf einen Bereich zwischen 0 und 1 normalisieren.

```python
# Plotten des Histogramms der MRT-Intensität
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignoriere den Hintergrund
im = im / im.max()  # Normalisiere
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensität (a.u.)')
ax1.set_ylabel('MRT-Dichte')
```
