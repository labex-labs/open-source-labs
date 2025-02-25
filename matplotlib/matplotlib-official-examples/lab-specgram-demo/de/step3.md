# Spektogramm generieren

Jetzt werden wir einen Spektogrammplot des Signals generieren. Wir werden die `specgram`-Methode aus der `Axes`-Klasse von Matplotlib verwenden, um das Spektogramm zu generieren. Diese Methode gibt vier Objekte zurück: `Pxx`, `freqs`, `bins` und `im`. `Pxx` ist das Periodogramm, `freqs` ist der Frequenzvektor, `bins` sind die Mittelpunkte der Zeitintervalle und `im` ist die `AxesImage`-Instanz, die die Daten im Plot darstellt.

```python
NFFT = 1024  # die Länge der Fenstersegmente
Fs = int(1.0 / dt)  # die Abtastfrequenz

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
