# カスタムコンテナを作る - 大いなる偽装

列にデータを格納すると、はるかにメモリを節約できますが、データを扱うのがかなり面倒になります。実際、演習2.2の以前の分析コードのどれも、列では機能しません。すべてが壊れてしまった理由は、以前の演習で使用されていたデータの抽象化を破ってしまったからです。つまり、データが辞書のリストとして格納されているという前提が崩れてしまったのです。

これは、「偽装」するカスタムコンテナオブジェクトを作ることで修正できます。それではやりましょう。

以前の分析コードは、データがレコードのシーケンスとして格納されていると仮定しています。各レコードは辞書として表されます。では、新しい「シーケンス」クラスを作り始めましょう。このクラスでは、`read_rides_as_columns()`関数で使用されていた4つのデータ列を格納します。

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # 列
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

`RideData`インスタンスを作成してみましょう。次のようなエラーメッセージが表示されて失敗することがわかります：

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

エラーメッセージを注意深く読んでください。それが何を実装する必要があるかを教えてくれます。では、`__len__()`と`__getitem__()`メソッドを追加しましょう。`__getitem__()`メソッドでは辞書を作成します。また、辞書を受け取り、それを4つの別々の`append()`操作に展開する`append()`メソッドも作成します。

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # 各値はすべての値のリスト（列）
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # すべてのリストは同じ長さであると仮定
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

これを正しく行えば、このオブジェクトを以前に書かれた`read_rides_as_dicts()`関数に投入できるはずです。コードを1行だけ変更するだけです：

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    バスの乗車データを辞書のリストとして読み込む
    '''
    records = RideData()      # <--- ここを変更
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # ヘッダーをスキップ
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

これを正しく行えば、古いコードは以前とまったく同じように機能するはずです。たとえば：

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

演習2.2の以前のCTAコードを実行してみましょう。修正することなく機能するはずですが、メモリを大幅に節約します。
