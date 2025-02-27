# Visualizar el árbol de decisión

También podemos visualizar el árbol de decisión utilizando la función `plot_tree` del módulo `tree` de scikit-learn.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
