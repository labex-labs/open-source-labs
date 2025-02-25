# 疑似画像を生成する

まず、NumPyの乱数モジュールを使って疑似グレースケール画像を生成します。結果を再現可能にするために、乱数の種を設定します。

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
