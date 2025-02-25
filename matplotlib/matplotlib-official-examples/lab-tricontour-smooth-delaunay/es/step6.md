# Mejorar la triangulación

Utilizamos un `TriAnalyzer` para mejorar la triangulación eliminando triángulos mal formados (planos) del borde de la triangulación. Luego aplicamos la máscara a la triangulación utilizando `set_mask`.

```python
# mascarando triángulos mal formados en el borde de la malla triangular.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
