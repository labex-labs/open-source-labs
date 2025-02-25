# Radii- und Winkelräume erstellen

Wir werden die Radii- und Winkelräume mit der `linspace`-Funktion erstellen:

```python
# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```
