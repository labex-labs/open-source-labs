# モデルの学習と選択

RFECVオブジェクトを作成し、交差検証スコアを計算します。スコアリング戦略「accuracy」は、正しく分類されたサンプルの割合を最適化します。推定器としてロジスティック回帰を使用し、5分割の層化k分割交差検証を行います。

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # 考慮する最小の特徴数
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Optimal number of features: {rfecv.n_features_}")
```
