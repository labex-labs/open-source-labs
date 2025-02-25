# Erstellen des Anfangsgraphen

Jetzt erstellen wir den Anfangsgraphen der Sinuswelle. Wir definieren die Anfangsparameter für die Amplitude und die Frequenz und zeichnen die Sinuswelle mit diesen Parametern.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
