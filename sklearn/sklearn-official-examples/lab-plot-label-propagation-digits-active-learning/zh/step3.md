# 训练标签传播模型

现在我们将使用有标签的数据点训练一个标签传播模型，并使用它来预测其余无标签数据点的标签。

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
