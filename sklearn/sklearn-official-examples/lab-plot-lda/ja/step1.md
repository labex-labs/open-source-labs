# ランダムなデータを生成する

まず、識別的な特徴とノイズのある特徴を持つランダムなデータを生成する必要があります。識別的な特徴1つで2つのクラスターのデータを生成するために、scikit - learnの`make_blobs`関数を使用します。その後、他の特徴にランダムなノイズを追加します。

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """ノイズのある特徴を持つランダムなブロブ状のデータを生成する。

    これは形状`(n_samples, n_features)`の入力データの配列と
    `n_samples`のターゲットラベルの配列を返す。

    識別的な情報を含むのは1つの特徴だけで、他の特徴はノイズのみを含む。
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # 識別的でない特徴を追加する
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
