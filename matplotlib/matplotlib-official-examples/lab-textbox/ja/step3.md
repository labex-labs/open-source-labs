# 送信関数を定義する

ユーザーがテキスト入力を送信したときに呼び出される`submit`関数を定義します。この関数は、ユーザーの入力に基づいて描画される関数を更新します。

```python
def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
