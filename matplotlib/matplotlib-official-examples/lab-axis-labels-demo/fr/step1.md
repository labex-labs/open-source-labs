# Import Matplotlib et créer un nuage de points

Nous commençons par importer Matplotlib et créer un nuage de points.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
