# Diagramme erstellen

Jetzt erstellen wir die Diagramme für unsere verschiedenen Spektrumdarstellungen. Wir verwenden die `subplots`-Funktion von Matplotlib, um ein 3x2-Gitter von Diagrammen zu erstellen. Wir werden das Zeit信号 im ersten Diagramm und die verschiedenen Spektrumtypen in den verbleibenden Diagrammen plotten.

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# Zeit信号 plotten:
axs[0, 0].set_title("Signal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Zeit")
axs[0, 0].set_ylabel("Amplitude")

# verschiedene Spektrumtypen plotten:
axs[1, 0].set_title("Amplitudenspektrum")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Logarithmisches Amplitudenspektrum")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Phasenspektrum ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Winkelspektrum")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # leeres Ax nicht anzeigen

fig.tight_layout()
plt.show()
```
