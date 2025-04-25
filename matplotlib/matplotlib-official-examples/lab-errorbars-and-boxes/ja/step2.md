# データの準備

次に、ボックスプロット用のデータを準備します。x 値と y 値、およびエラー値のダミーデータを作成します。

```python
# データポイントの数
n = 5

# ダミーデータ
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# ダミーエラー（上下）
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
