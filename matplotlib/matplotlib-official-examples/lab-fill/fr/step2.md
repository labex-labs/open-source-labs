# Définir la fonction du flocon de Koch

Ensuite, nous allons définir une fonction pour générer le flocon de Koch. La fonction prend deux paramètres : la profondeur de récursion et le facteur d'échelle.

```python
def koch_snowflake(order, scale=10):
    """
    Retourne deux listes x, y des coordonnées des points du flocon de Koch.

    Paramètres
    ----------
    order : int
        La profondeur de récursion.
    scale : float
        L'étendue du flocon (longueur du côté du triangle de base).
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # triangle initial
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # points de départ
            p2 = np.roll(p1, shift=-1)  # points d'arrivée
            dp = p2 - p1  # vecteurs de connexion

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y
```
