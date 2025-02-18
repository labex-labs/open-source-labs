# スコープクラスの設定

Scope クラスは、オシロスコープを作成するために必要なデータとメソッドを保持します。コンストラクタでは、必要な変数を初期化し、プロットを設定します。

```python
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
```
