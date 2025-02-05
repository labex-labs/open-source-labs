# 交叉验证估计器

scikit-learn 中的一些估计器具有内置的交叉验证功能。这些经过交叉验证的估计器通过交叉验证自动选择其参数，从而使模型选择过程更加高效。

```python
from sklearn import linear_model, datasets

# 创建一个 LassoCV 对象
lasso = linear_model.LassoCV()

# 加载糖尿病数据集
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# 在数据集上拟合 LassoCV 对象
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
