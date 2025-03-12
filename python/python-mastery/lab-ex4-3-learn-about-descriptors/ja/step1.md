# ディスクリプタプロトコルの理解

このステップでは、簡単な `Stock` クラスを作成することで、Python のディスクリプタがどのように動作するかを学びます。Python のディスクリプタは、属性のアクセス、設定、削除方法をカスタマイズできる強力な機能です。ディスクリプタプロトコルは、`__get__()`、`__set__()`、`__delete__()` という 3 つの特殊メソッドで構成されています。これらのメソッドは、それぞれ属性がアクセスされたとき、値が割り当てられたとき、削除されたときのディスクリプタの動作を定義します。

まず、プロジェクトディレクトリに `stock.py` という新しいファイルを作成する必要があります。このファイルには `Stock` クラスを記述します。以下は `stock.py` ファイルに記述するコードです。

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

この `Stock` クラスでは、`property` デコレータを使用して、`name`、`shares`、`price` 属性のゲッターとセッターメソッドを定義しています。これらのゲッターとセッターメソッドはディスクリプタとして機能し、これらの属性のアクセスと設定方法を制御します。たとえば、セッターメソッドは入力値を検証し、正しい型であり、許容範囲内であることを確認します。

`stock.py` ファイルが準備できたら、Python シェルを開いて `Stock` クラスを試し、ディスクリプタが実際にどのように動作するかを確認しましょう。これを行うには、ターミナルを開き、以下のコマンドを実行します。

```bash
cd ~/project
python3 -i stock.py
```

`python3` コマンドの `-i` オプションは、`stock.py` ファイルを実行した後に対話型シェルを起動するよう Python に指示します。これにより、先ほど定義した `Stock` クラスと直接対話できます。

Python シェルで、株式オブジェクトを作成し、その属性にアクセスしてみましょう。以下のように操作できます。

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

`s` オブジェクトの `name` と `shares` 属性にアクセスするとき、Python は実際にはディスクリプタの `__get__` メソッドを内部で使用しています。クラス内の `property` デコレータはディスクリプタを使用して実装されており、属性のアクセスと割り当てを制御します。

ディスクリプタオブジェクトを確認するために、クラス辞書を詳しく見てみましょう。クラス辞書には、クラスで定義されたすべての属性とメソッドが含まれています。以下のコードを使用して、クラス辞書のキーを表示できます。

```python
Stock.__dict__.keys()
```

以下のような出力が表示されるはずです。

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

`name`、`shares`、`price` のキーは、`property` デコレータによって作成されたディスクリプタオブジェクトを表しています。

次に、ディスクリプタのメソッドを手動で呼び出すことで、ディスクリプタがどのように動作するかを調べてみましょう。`shares` ディスクリプタを例に説明します。以下のように操作できます。

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

`s.shares` のように属性にアクセスするとき、Python はディスクリプタの `__get__` メソッドを呼び出して値を取得します。`s.shares = 75` のように値を割り当てるとき、Python はディスクリプタの `__set__` メソッドを呼び出します。ディスクリプタはデータを検証し、入力値が無効な場合はエラーを発生させます。

`Stock` クラスとディスクリプタの実験が終了したら、以下のコマンドを実行して Python シェルを終了できます。

```python
exit()
```
