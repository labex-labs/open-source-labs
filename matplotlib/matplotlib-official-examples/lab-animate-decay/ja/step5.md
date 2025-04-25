# アニメーション関数を定義する

次に、アニメーションの各フレームに対してグラフを更新する関数を定義する必要があります。この関数は、`data_gen()`関数で生成されたデータを受け取り、新しいデータでグラフを更新します。また、アニメーションが進行するにつれて x 軸の範囲も更新します。

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
