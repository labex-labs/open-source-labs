# Signale generieren

Als nächstes werden wir zwei Signale mit einem kohärenten Anteil bei 10 Hz und einem zufälligen Anteil generieren. Wir werden auch weißes Rauschen zu den Signalen hinzufügen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2
```
