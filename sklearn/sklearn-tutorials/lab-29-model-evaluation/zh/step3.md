# 指标函数

scikit-learn 的 `metrics` 模块实现了几个用于特定目的评估预测误差的函数。这些函数可用于计算模型预测的质量。

以下是使用 `metrics` 模块中的 `accuracy_score` 函数的示例：

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
