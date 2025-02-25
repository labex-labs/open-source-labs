# Personnaliser le graphique

Nous pouvons personnaliser le graphique en ajoutant des titres, des étiquettes d'axe et des cartes de couleurs.

```python
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.set_title('Signal dans le domaine temporel')
ax1.set_xlabel('Temps (s)')
ax1.set_ylabel('Amplitude')
ax1.plot(t, x)

ax2.set_title('Spectrogramme')
ax2.set_xlabel('Temps (s)')
ax2.set_ylabel('Fréquence (Hz)')
im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900, cmap='viridis')
fig.colorbar(im[3], ax=ax2)
```
