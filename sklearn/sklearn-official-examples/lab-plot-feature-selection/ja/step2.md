# 単変量特徴選択

次に、F 検定を用いて特徴の評点付けを行う単変量特徴選択を行います。4 つの最も重要な特徴を選択するためにデフォルトの選択関数を使用します。

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
