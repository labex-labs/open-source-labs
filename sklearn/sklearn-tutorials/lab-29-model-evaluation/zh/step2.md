# 评分参数

Scikit-learn 在一些模型评估工具中提供了一个“scoring”参数，比如交叉验证和网格搜索。“scoring”参数控制在评估期间应用于估计器的指标。

以下是在交叉验证中使用“scoring”参数的示例：

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
