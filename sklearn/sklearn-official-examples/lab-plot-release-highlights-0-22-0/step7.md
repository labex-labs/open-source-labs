# Tree pruning

It is now possible to prune most tree-based estimators once the trees are built. The pruning is based on minimal cost-complexity.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(random_state=0)

rf = RandomForestClassifier(random_state=0, ccp_alpha=0).fit(X, y)
print(
    "Average number of nodes without pruning {:.1f}".format(
        np.mean([e.tree_.node_count for e in rf.estimators_])
    )
)

rf = RandomForestClassifier(random_state=0, ccp_alpha=0.05).fit(X, y)
print(
    "Average number of nodes with pruning {:.1f}".format(
        np.mean([e.tree_.node_count for e in rf.estimators_])
    )
)
```
