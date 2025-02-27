# Daten erstellen

Wir werden einige Daten erstellen, die zum Veranschaulichen des Ver光栅isierungsbegriffs verwendet werden.

```python
d = np.arange(100).reshape(10, 10)  # die Werte, die farbzugeordnet werden sollen
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # drehe x um -theta
yy = x*np.sin(theta) + y*np.cos(theta)  # drehe y um -theta
```