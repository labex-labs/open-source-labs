# 回帰モデルのフィット

次に、線形、多項式、およびRBFカーネルを使用して、サンプルデータセットに対してSVRモデルをフィットさせます。各モデルのハイパーパラメータを設定し、サンプルデータセットで学習させます。

```python
from sklearn.svm import SVR

# Fit regression model
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
