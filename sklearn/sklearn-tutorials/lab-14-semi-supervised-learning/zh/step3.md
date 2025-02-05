# 标签传播

## 标签传播算法概述

标签传播是一种半监督图推理算法。它在输入数据集中的所有项上构建一个相似性图，并使用此图将标签从已标记数据传播到未标记数据。标签传播可用于分类任务，并支持核方法将数据投影到替代维度空间。

## 在scikit-learn中使用标签传播

在scikit-learn中，有两种可用的标签传播模型：`LabelPropagation`和`LabelSpreading`。这两种模型都构建一个相似性图并传播标签。以下是使用标签传播的示例：

```python
from sklearn.semi_supervised import LabelPropagation

# 创建一个标签传播模型
label_propagation = LabelPropagation()

# 在已标记数据上训练标签传播模型
label_propagation.fit(X_labeled, y_labeled)

# 预测新样本的标签
y_pred = label_propagation.predict(X_test)
```

在上述示例中，`X_labeled`和`y_labeled`是已标记数据，`X_test`是要预测的新样本。
