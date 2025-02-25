# Berechne das elektrische Feld

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Erklärung:

- `CubicTriInterpolator` ist eine Klasse, die Daten mithilfe eines kubischen Polynoms interpoliert.
- `tci` ist eine Instanz der `CubicTriInterpolator`-Klasse.
- `(Ex, Ey)` ist das elektrische Feld.
- `E_norm` ist das normalisierte elektrische Feld.
