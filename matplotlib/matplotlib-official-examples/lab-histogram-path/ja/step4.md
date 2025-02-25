# 長方形の角を生成する

長方形を使ってヒストグラムを描画するには、各長方形の角を計算する必要があります。次のコードを追加します。

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
