# クラスの定義

データをダウンサンプリングし、ズーム操作時に再計算する `DataDisplayDownsampler` というクラスを定義します。このクラスのコンストラクタは、xdata と ydata を入力パラメータとして受け取ります。最大ポイント数を 50 に設定し、xdata の差分を計算します。

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
