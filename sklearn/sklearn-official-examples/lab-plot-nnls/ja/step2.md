# データを学習用とテスト用に分割する

データを学習用セットとテスト用セットに分割します。それぞれのセットにデータの 50％を割り当てます。

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
