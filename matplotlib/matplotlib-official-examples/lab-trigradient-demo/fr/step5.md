# Calculer le champ électrique

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Explication :

- `CubicTriInterpolator` est une classe qui interpole des données en utilisant un polynôme cubique.
- `tci` est une instance de la classe `CubicTriInterpolator`.
- `(Ex, Ey)` est le champ électrique.
- `E_norm` est le champ électrique normalisé.
