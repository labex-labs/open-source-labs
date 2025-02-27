# グリッドサーチ

グリッドサーチは、推定器のパラメータ値の最適な組み合わせを見つけるために使用できる手法です。これには、パラメータ値のグリッドを指定し、各パラメータの組み合わせに対して学習データに推定器を適合させ、最も高い交差検証スコアをもたらすパラメータを選択することが含まれます。

```python
from sklearn.model_selection import GridSearchCV

# パラメータ値のグリッドを定義する
Cs = np.logspace(-6, -1, 10)

# SVM 分類器とパラメータグリッドを持つ GridSearchCV オブジェクトを作成する
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# GridSearchCV オブジェクトを学習データに適合させる
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
