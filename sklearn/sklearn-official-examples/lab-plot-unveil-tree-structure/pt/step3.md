# Visualizar a Árvore de Decisão

Também podemos visualizar a árvore de decisão usando a função `plot_tree` do módulo `tree` do scikit-learn.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
