# テキストを描画する

これでテキストが定義できたので、Matplotlibを使って描画できます。このステップでは、グラフを作成し、`fig.text()` メソッドを使ってそのグラフにテキストを追加します。

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
