# Visualize the Decision Tree

We can also visualize the decision tree using the `plot_tree` function from scikit-learn's `tree` module.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
