# Créez l'axe secondaire

Nous allons maintenant créer l'axe secondaire et convertir l'axe des abscisses des degrés en radians. Nous utiliserons `deg2rad` comme fonction de conversion directe et `rad2deg` comme fonction inverse.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
