# 前処理ステップと分類器を備えた単純なパイプラインの構築

このステップでは、前処理ステップと分類器を備えた単純なパイプラインを構築し、その視覚的表現を表示します。

まず、必要なモジュールをインポートします。

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

次に、パイプラインのステップを定義します。

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

そして、パイプラインを作成します。

```python
pipe = Pipeline(steps)
```

最後に、パイプラインの視覚的表現を表示します。

```python
set_config(display="diagram")
pipe
```
