# 決定木を可視化する

scikit-learnの`tree`モジュールの`plot_tree`関数を使って、決定木を可視化することもできます。

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
