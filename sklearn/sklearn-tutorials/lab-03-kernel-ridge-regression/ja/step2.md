# 疑似データの生成

次に、使用する疑似データを生成しましょう。正弦波の目的関数を作成し、それにいくらかのランダムノイズを追加します。

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
