# Daten generieren

Als nächstes werden wir die Daten generieren, die wir verwenden werden, um das Gittersdiagramm zu erstellen. In diesem Lab werden wir die Funktion `np.meshgrid()` verwenden, um die X-, Y- und Z-Koordinaten zu erstellen.

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
