# その他のデータ構造のメモリ使用量

Pythonには、データ構造を表現するためのさまざまな選択肢があります。たとえば：

```python
# タプル
row = (route, date, daytype, rides)

# 辞書
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# クラス
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# 名前付きタプル
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# __slots__ を持つクラス
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

あなたのタスクは以下の通りです。これらのデータ構造のそれぞれを使って1行のデータを表現する `read_rides()` 関数の異なるバージョンを作成します。そして、各オプションの結果としてのメモリ使用量を調べます。一度に大量のデータを扱う場合、最も効率的な格納方法はどれかを見つけましょう。
