# Rotular cada plano de visualização 3D primário

Usamos a função `annotate_axes` definida no passo 2 para rotular cada plano de visualização 3D primário com seus respectivos ângulos.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
