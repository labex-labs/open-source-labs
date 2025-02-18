# Den Lorenz-Attraktor berechnen

Wir berechnen den Lorenz-Attraktor, indem wir uns durch die Zeit bewegen und den nächsten Punkt anhand des vorherigen Punkts und der Lorenz-Funktion schätzen.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
