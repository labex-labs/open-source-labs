# Definieren der Daten

Wir werden die Daten für das Diagramm definieren. Wir werden 20 zufällige Werte für Radien und Winkel generieren.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```
