# データの分割

scikit-learn の `train_test_split` 関数を使用して、データを訓練データセットとテストデータセットに分割します。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
