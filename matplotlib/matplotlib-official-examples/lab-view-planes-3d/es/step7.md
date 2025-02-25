# Etiquetar cada plano principal de vista tridimensional

Usamos la función `annotate_axes` definida en el paso 2 para etiquetar cada plano principal de vista tridimensional con sus respectivos ángulos.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
