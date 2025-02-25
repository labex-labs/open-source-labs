# Générer le spectrogramme

Maintenant, nous allons générer un graphique de spectrogramme du signal. Nous allons utiliser la méthode `specgram` de la classe `Axes` de Matplotlib pour générer le spectrogramme. Cette méthode renvoie quatre objets : `Pxx`, `freqs`, `bins` et `im`. `Pxx` est le spectrogramme, `freqs` est le vecteur de fréquences, `bins` est le centre des intervalles temporels, et `im` est l'instance `AxesImage` représentant les données dans le graphique.

```python
NFFT = 1024  # la longueur des segments de fenêtrage
Fs = int(1.0 / dt)  # la fréquence d'échantillonnage

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
