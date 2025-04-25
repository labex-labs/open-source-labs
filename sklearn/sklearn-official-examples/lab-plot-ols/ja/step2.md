# データセットを分割する

次に、データセットを訓練用とテスト用に分割します。データの 80％を訓練に、20％をテストに使用します。

```python
# データを訓練用/テスト用に分割する
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# ターゲットを訓練用/テスト用に分割する
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
