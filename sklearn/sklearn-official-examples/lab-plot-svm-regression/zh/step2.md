# 拟合回归模型

接下来，我们使用线性、多项式和径向基函数（RBF）内核为我们的样本数据集拟合一个支持向量回归（SVR）模型。我们为每个模型设置超参数，并在我们的样本数据集上对它们进行训练。

```python
from sklearn.svm import SVR

# 拟合回归模型
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
