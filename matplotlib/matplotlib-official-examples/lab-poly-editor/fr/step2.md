# Créez une fonction pour calculer la distance

Nous devons créer une fonction qui calcule la distance entre un point et un segment de ligne. Cette fonction sera utilisée plus tard pour déterminer si un nouveau sommet doit être ajouté au polygone.

```python
def dist_point_to_segment(p, s0, s1):
    """
    Obtenez la distance entre le point *p* et le segment (*s0*, *s1*), où
    *p*, *s0*, *s1* sont des tableaux ``[x, y]``.
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # Projetez sur le segment, sans dépasser les extrémités du segment.
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))
```
