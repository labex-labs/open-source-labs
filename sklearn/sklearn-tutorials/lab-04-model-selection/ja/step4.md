# 交差検証付き推定器

scikit-learn の一部の推定器には、組み込みの交差検証機能があります。これらの交差検証付き推定器は、交差検証によって自動的にパラメータを選択し、モデル選択プロセスをより効率的にします。

```python
from sklearn import linear_model, datasets

# LassoCV オブジェクトを作成する
lasso = linear_model.LassoCV()

# 糖尿病データセットを読み込む
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# LassoCV オブジェクトをデータセットに適合させる
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
