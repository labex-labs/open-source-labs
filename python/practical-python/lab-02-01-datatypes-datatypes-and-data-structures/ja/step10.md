# なぜ辞書が必要なのか？

様々な値があり、それらの値を変更または操作する必要がある場合、辞書は便利です。辞書を使うことでコードが読みやすくなります。

```python
s['price']
# vs
s[2]
```

ここ数回のエクササイズでは、`portfolio.csv` というデータファイルを読み込むプログラムを書きました。`csv` モジュールを使えば、ファイルを 1 行ずつ読み込むことが簡単です。

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name','shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

ファイルを読み込むことは簡単ですが、データに対して読み込むだけでなく、さらに多くのことを行いたい場合があります。たとえば、データを保存してからそれに対して計算を行いたいかもしれません。残念ながら、データの生の「行」だけでは十分な作業ができません。たとえば、単純な数学の計算でさえうまくいきません。

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

さらに多くのことを行うには、通常、生のデータを何らかの方法で解釈し、後で使えるようにもっと便利な種類のオブジェクトに変換する必要があります。2 つの簡単なオプションはタプルまたは辞書です。
