# 可视化决策树

我们还可以使用scikit-learn的`tree`模块中的`plot_tree`函数来可视化决策树。

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
