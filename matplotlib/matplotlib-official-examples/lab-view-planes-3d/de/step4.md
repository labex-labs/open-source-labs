# Definieren des Layouts des 3D-Diagramms

Wir definieren das Layout des 3D-Diagramms mithilfe einer Liste von Listen. Das `'.'` in der Liste stellt ein leeres Subplot dar.

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```
