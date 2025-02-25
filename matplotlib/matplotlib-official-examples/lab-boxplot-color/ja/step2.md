# ランダムなテストデータの作成

次に、`numpy` ライブラリを使ってランダムなテストデータを作成します。標準偏差の異なる3セットのデータを生成します。

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
