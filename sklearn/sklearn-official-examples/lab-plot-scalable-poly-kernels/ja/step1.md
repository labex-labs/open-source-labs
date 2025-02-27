# データの読み込みと準備

まず、Covtype データセットを読み込み、1 つのクラスのみを選択することで 2 値分類問題に変換します。その後、データを訓練セットとテストセットに分割し、特徴を正規化します。

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Covtype データセットを読み込み、1 つのクラスのみを選択
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# データを訓練セットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# 特徴を正規化
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
