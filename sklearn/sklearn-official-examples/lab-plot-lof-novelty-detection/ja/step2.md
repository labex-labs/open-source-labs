# データの生成

numpy を使用して、トレーニング用、テスト用、および外れ値用のデータを生成します。100 個の通常のトレーニング観測値、20 個の通常のテスト観測値、および 20 個の異常な新奇観測値を生成します。

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
