# Создаем пространства радиусов и углов

Мы создадим пространства радиусов и углов с использованием функции `linspace`:

```python
# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```
