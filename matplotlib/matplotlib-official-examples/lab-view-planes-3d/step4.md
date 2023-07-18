# Define the layout of the 3D plot

We define the layout of the 3D plot using a list of lists. The `'.'` in the list represents an empty subplot.

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```
