# データセットを学習用とテスト用に分割する

次に、scikit-learnの`train_test_split`関数を使ってデータセットを学習用とテスト用に分割します。学習にはデータの90%を、テストには10%を使います。

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
