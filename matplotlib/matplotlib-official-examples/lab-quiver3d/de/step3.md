# Die Richtung der Pfeile definieren

Jetzt definieren wir die Richtung der Pfeile. In diesem Beispiel definieren wir die Richtung der Pfeile mit Hilfe der trigonometrischen Funktionen von NumPy. Die `sin`- und `cos`-Funktionen werden verwendet, um die `u`, `v` und `w`-Arrays zu erstellen, die die Richtung der Pfeile in den `x`, `y` und `z`-Richtungen repräsentieren.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
