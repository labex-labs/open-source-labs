# 次元削減と分類器を備えたパイプラインの構築

このステップでは、次元削減ステップと分類器を備えたパイプラインを構築し、その視覚的表現を表示します。

まず、必要なモジュールをインポートします。

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
```

次に、パイプラインのステップを定義します。

```python
steps = [("reduce_dim", PCA(n_components=4)), ("classifier", SVC(kernel="linear"))]
```

そして、パイプラインを作成します。

```python
pipe = Pipeline(steps)
```

最後に、パイプラインの視覚的表現を表示します。

```python
pipe
```
