# Erstellen eines Gitters

Wir erstellen ein Gitter im Raum der Parameterisierungsvariablen `u` und `v`. Dies wird mit der Funktion `np.meshgrid()` durchgeführt, um ein Gitter von `u`- und `v`-Punkten zu erstellen.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
