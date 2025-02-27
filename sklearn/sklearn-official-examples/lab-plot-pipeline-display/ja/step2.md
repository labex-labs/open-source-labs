# 複数の前処理ステップと分類器を連鎖させたパイプラインの構築

このステップでは、複数の前処理ステップと分類器を備えたパイプラインを構築し、その視覚的表現を表示します。

まず、必要なモジュールをインポートします。

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
```

次に、パイプラインのステップを定義します。

```python
steps = [
    ("standard_scaler", StandardScaler()),
    ("polynomial", PolynomialFeatures(degree=3)),
    ("classifier", LogisticRegression(C=2.0)),
]
```

そして、パイプラインを作成します。

```python
pipe = Pipeline(steps)
```

最後に、パイプラインの視覚的表現を表示します。

```python
pipe
```
