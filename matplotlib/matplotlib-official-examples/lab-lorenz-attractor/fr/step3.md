# Configuration des paramètres initiaux

Nous configurons les paramètres initiaux pour la simulation, y compris le pas de temps `dt`, le nombre de pas `num_steps` et les valeurs initiales pour `x`, `y` et `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```
