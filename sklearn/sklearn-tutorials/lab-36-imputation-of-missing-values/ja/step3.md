# IterativeImputerを使った多変量特徴量の欠損値補完

`IterativeImputer`クラスは、欠損値を補完するためのより高度なアプローチです。欠損値を持つ各特徴量を他の特徴量の関数としてモデル化し、その推定値を欠損値補完に使用します。特徴量間の関係を反復的に学習し、これらの関係に基づいて欠損値を補完します。

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
