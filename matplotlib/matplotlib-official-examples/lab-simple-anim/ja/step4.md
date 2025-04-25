# アニメーション関数の定義

アニメーション関数は、`FuncAnimation()`関数によって呼び出され、新しいデータでグラフを更新するために使用されます。この例では、時間とともに振幅が変化するサイン波で折れ線グラフの y 軸の値を更新します。

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```
