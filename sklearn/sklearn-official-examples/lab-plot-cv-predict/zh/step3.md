# 生成交叉验证预测

我们将使用scikit-learn中的`cross_val_predict`函数来生成交叉验证预测。

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
