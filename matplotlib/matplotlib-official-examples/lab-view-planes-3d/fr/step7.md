# Étiquetez chaque plan de vue principal 3D

Nous utilisons la fonction `annotate_axes` définie dans l'étape 2 pour étiqueter chaque plan de vue principal 3D avec ses angles respectifs.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
