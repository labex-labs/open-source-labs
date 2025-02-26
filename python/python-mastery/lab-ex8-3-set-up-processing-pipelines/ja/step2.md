# いくつかのパイプラインコンポーネントを作成する

`coticker.py` というファイルに、演習8.2の `ticker.py` プログラムと同じタスクを行う一連のパイプラインコンポーネントを作成します。以下は、さまざまな部分の実装です。

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price =Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv

# これは厄介です。解説については解説を参照してください
@consumer
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

あなたのチャレンジ：前の演習と同じ株価チケッカーを生成するために、これらすべてのコンポーネントを結び付けるメインプログラムを書くことです。
