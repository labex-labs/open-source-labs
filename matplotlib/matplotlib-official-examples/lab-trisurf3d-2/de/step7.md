# Abbilden auf `x`, `y`, `z`-Punkte

Wir projizieren die `radius`-`angle`-Paare auf `x`, `y`, `z`-Punkte.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
