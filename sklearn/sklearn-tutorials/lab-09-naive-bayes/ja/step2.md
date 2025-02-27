# データセットを学習用とテスト用に分割する

次に、`sklearn.model_selection`モジュールの`train_test_split`関数を使って、データセットを学習用とテスト用に分割します。学習用セットはナイーブベイズ分類器を訓練するために使用され、テスト用セットはその性能を評価するために使用されます。

```python
from sklearn.model_selection import train_test_split

# データセットを学習用とテスト用に分割する
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
