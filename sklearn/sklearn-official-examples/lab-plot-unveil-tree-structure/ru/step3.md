# Визуализировать дерево решений

Мы также можем визуализировать дерево решений с использованием функции `plot_tree` из модуля `tree` в scikit - learn.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
