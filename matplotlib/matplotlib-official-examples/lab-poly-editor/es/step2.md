# Crear una función para calcular la distancia

Necesitamos crear una función que calcule la distancia entre un punto y un segmento de línea. Esta función se utilizará más adelante para determinar si se debe agregar un nuevo vértice al polígono.

```python
def dist_point_to_segment(p, s0, s1):
    """
    Obtener la distancia desde el punto *p* hasta el segmento (*s0*, *s1*), donde
    *p*, *s0*, *s1* son arrays ``[x, y]``.
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # Proyectar sobre el segmento, sin pasar los extremos del segmento.
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))
```
