# データの生成

私たちは、ペナルティを適用するためのサンプル データを生成します。この例では、それぞれ 100 個のサンプルを持つ 2 つのクラスのデータを生成します。

```python
np.random.seed(42)

# Generate two classes of data
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
