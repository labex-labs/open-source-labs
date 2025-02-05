# 评分与交叉验证评分

scikit-learn 中的估计器公开了一个 `score` 方法，可用于评估模型对新数据的拟合质量或预测质量。此方法返回一个分数，分数越高表示性能越好。

```python
from sklearn import datasets, svm

# 加载数字数据集
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# 创建一个具有线性核的支持向量机分类器
svc = svm.SVC(C=1, kernel='linear')

# 在训练数据上拟合分类器，并计算在测试数据上的分数
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

为了更好地衡量预测准确性，我们可以使用交叉验证。交叉验证包括将数据拆分为多个折，将每个折用作测试集，其余折用作训练集。此过程重复多次，并对分数求平均值以获得整体性能。

```python
import numpy as np

# 将数据拆分为3折
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# 执行交叉验证
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
