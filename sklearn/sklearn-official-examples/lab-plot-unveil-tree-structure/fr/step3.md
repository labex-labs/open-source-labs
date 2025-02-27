# Visualiser l'arbre de décision

Nous pouvons également visualiser l'arbre de décision à l'aide de la fonction `plot_tree` du module `tree` de scikit-learn.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
