# exec() の基本を理解する

Python では、`exec()` 関数は実行時に動的に作成されたコードを実行することができる強力なツールです。これは、特定の入力や設定に基づいてコードを即座に生成できることを意味し、多くのプログラミングシナリオで非常に有用です。

まずは、`exec()` 関数の基本的な使い方を探ってみましょう。これを行うには、Python シェルを開きます。ターミナルを開き、`python3` と入力します。このコマンドにより、Python コードを直接実行できる対話型 Python インタープリターが起動します。

```bash
python3
```

ここで、Python コードの一部を文字列として定義し、`exec()` 関数を使ってそれを実行します。以下はその動作方法です。

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

この例では：

1. まず、`code` という名前の文字列を定義しました。この文字列には Python の for ループが含まれています。このループは `n` 回繰り返され、各繰り返しの番号を出力するように設計されています。
2. 次に、変数 `n` を定義し、値 10 を割り当てました。この変数は、ループ内の `range()` 関数の上限として使用されます。
3. その後、`exec()` 関数を呼び出し、引数として `code` 文字列を渡しました。`exec()` 関数はこの文字列を受け取り、それを Python コードとして実行します。
4. 最後に、ループが実行され、0 から 9 までの数字が出力されました。

`exec()` 関数の本当の威力は、関数やメソッドなど、より複雑なコード構造を作成する際により明らかになります。クラスの `__init__()` メソッドを動的に作成する、より高度な例を試してみましょう。

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

このより複雑な例では：

1. まず、`_fields` 属性を持つ `Stock` クラスを定義しました。この属性は、クラスの属性名を含むタプルです。
2. 次に、`__init__` メソッドの Python コードを表す文字列を作成しました。このメソッドは、オブジェクトの属性を初期化するために使用されます。
3. その後、`exec()` 関数を使ってコード文字列を実行しました。また、空の辞書 `locs` を `exec()` に渡しました。実行結果の関数はこの辞書に格納されます。
4. その後、辞書に格納された関数を `Stock` クラスの `__init__` メソッドとして割り当てました。
5. 最後に、`Stock` クラスのインスタンスを作成し、オブジェクトの属性にアクセスすることで `__init__` メソッドが正しく動作することを確認しました。

この例は、`exec()` 関数が実行時に利用可能なデータに基づいてメソッドを動的に作成するためにどのように使用できるかを示しています。
