# 演習 2.16: zip() 関数の使用

ファイル `portfolio.csv` の最初の行には列ヘッダが含まれています。これまでのコードでは、それらを捨ててきました。

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>>
```

しかし、ヘッダを何か役に立つことに使えないでしょうか？ここで `zip()` 関数が登場します。まず、ファイルのヘッダとデータの 1 行をペアにするためにこれを試してみましょう。

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

`zip()` が列ヘッダと列値をどのようにペアにしたかに注目してください。ここでは結果をリストに変換するために `list()` を使っています。これにより結果を見ることができます。通常、`zip()` はイテレータを作成し、for ループで消費する必要があります。

このペアリングは辞書を作成するための中間ステップです。次にこれを試してみましょう。

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

この変換は、多くのデータファイルを処理する際に知っておく最も便利なトリックの 1 つです。たとえば、`pcost.py` プログラムをさまざまな入力ファイルで動作させたいが、名前、株数、価格が表示される実際の列番号を考慮しない場合があります。

`pcost.py` の `portfolio_cost()` 関数を次のように変更します。

```python
# pcost.py

def portfolio_cost(filename):
  ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # これは上の int() と float() 変換のエラーをキャッチします
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
      ...
```

次に、まったく異なるデータファイル `portfoliodate.csv` で関数を試してみましょう。このファイルは次のようになっています。

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

正しく行えば、データファイルの列形式が以前とまったく異なっていてもプログラムがまだ機能することがわかります。すごいですね！

ここで行われた変更は微妙ですが、重要です。`portfolio_cost()` が単一の固定ファイル形式を読み取るようにハードコードされていたのではなく、新しいバージョンは任意の CSV ファイルを読み取り、その中から関心のある値を抽出します。ファイルに必要な列があれば、コードは機能します。

セクション 2.3 で書いた `report.py` プログラムを変更して、同じ手法を使って列ヘッダを抽出するようにします。

`report.py` プログラムを `portfoliodate.csv` ファイルで実行して、以前と同じ結果が得られることを確認してみましょう。
