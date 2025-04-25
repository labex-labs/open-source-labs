# データの読み込みと準備

scikit-learn からワインのデータセットを読み込み、学習用とテスト用のセットに分割します。また、scikit-learn の前処理モジュールからの StandardScaler を使って、学習用セットの特徴量をスケーリングします。

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```
