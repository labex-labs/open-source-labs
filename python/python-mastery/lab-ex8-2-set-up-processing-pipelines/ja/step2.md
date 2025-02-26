# さらにパイプラインコンポーネントを作成する

`ticker.py` というファイルに、次のクラスを定義し（以前の構造コードを使用して）、パイプラインを設定します。

```python
# ticker.py

from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

これを実行すると、次のような出力が表示されるはずです。

    Ticker('IBM',103.53,'6/11/2007','09:53.59',0.46,102.87,103.53,102.77,541633)
    Ticker('MSFT',30.21,'6/11/2007','09:54.01',0.16,30.05,30.21,29.95,7562516)
    Ticker('AA',40.01,'6/11/2007','09:54.01',0.35,39.67,40.15,39.31,576619)
    Ticker('T',40.1,'6/11/2007','09:54.08',-0.16,40.2,40.19,39.87,1312959)
