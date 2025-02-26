# 合理的にする

ミックスインを使用することは、必要なコード量を削減するためにフレームワークのビルダーにとって役立つツールです。ただし、ユーザーにクラスを適切に組み合わせて多重継承を使用する方法を覚えさせることは、彼らの頭を混乱させる可能性があります。演習3.5では、カスタムフォーマッタを作成するのを簡単にする関数`create_formatter()`を書きました。その関数を持ち、ミックスインクラスに関連するいくつかのオプション引数を理解するように拡張します。たとえば：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

内部的には、`create_formatter()`関数はクラスを適切に組み合わせ、適切な`TableFormatter`インスタンスを返します。
