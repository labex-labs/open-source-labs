# Définissez une fonction pour obtenir le point d'une ligne verticale tournée

Nous allons définir une fonction qui prend les coordonnées d'origine, la longueur de la ligne et l'angle en degrés en entrée et renvoie les coordonnées xy de l'extrémité de la ligne verticale tournée de l'angle spécifié.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Renvoie les coordonnées xy de l'extrémité de la ligne verticale tournée de degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
