# Diffusion (broadcasting) avec une valeur scalaire

La diffusion (broadcasting) permet également d'effectuer des opérations élément par élément entre un tableau et une valeur scalaire. La valeur scalaire est automatiquement « étirée » pour correspondre à la forme du tableau. Par exemple :

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
result = a * b
```

Dans ce cas, `b` est une valeur scalaire, mais elle est étirée pour devenir un tableau ayant la même forme que `a`. La multiplication est ensuite effectuée élément par élément, donnant `[2.0, 4.0, 6.0]`.
