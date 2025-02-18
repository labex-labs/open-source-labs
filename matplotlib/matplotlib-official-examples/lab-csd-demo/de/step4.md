# Kreuzspektraldichte (CSD) berechnen

Um die Kreuzspektraldichte (Cross Spectral Density, CSD) von zwei Signalen zu berechnen, müssen wir die csd-Funktion von Matplotlib verwenden. Die Funktion nimmt die beiden Signale, die Anzahl der Punkte für die schnelle Fourier-Transformation (FFT) und die Abtastfrequenz als Eingaben.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
