# 相互情報量の計算

ここで、各特徴量に対する相互情報量のスコアを計算します。相互情報量は、変数間のあらゆる種類の依存関係を捉えることができます。相互情報量のスコアを最大の相互情報量スコアで割ることにより、正規化します。

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
