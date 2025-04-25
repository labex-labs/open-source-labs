# データセットとモデル

2 種類のアヤメを識別するために、アヤメのデータセットと線形サポートベクター分類器（Linear SVC）を使用します。まず、必要なライブラリをインポートしてデータセットを読み込みます。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

次に、データセットにノイズ付きの特徴量を追加し、訓練用とテスト用のセットに分割します。

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

最後に、StandardScaler を使ってデータをスケーリングし、訓練データに線形サポートベクター分類器を適合させます。

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
