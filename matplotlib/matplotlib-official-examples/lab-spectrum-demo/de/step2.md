# Variablen festlegen

Als nächstes legen wir die Variablen für unser Signal fest. Wir verwenden einen Abtastintervall von 0,01, was uns eine Abtastfrequenz von 100 Hz liefert. Wir erstellen ein Zeitarray von 0 bis 10 Sekunden mit einem Schritt von 0,01 Sekunden. Wir generieren auch Rauschen mithilfe der `randn`-Funktion von NumPy und verketten es mit einer Exponentialabfallfunktion, um ein rauschendes Signal zu erstellen.

```python
np.random.seed(0)

dt = 0.01  # Abtastintervall
Fs = 1 / dt  # Abtastfrequenz
t = np.arange(0, 10, dt)

# Rauschen generieren:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # das Signal
```
