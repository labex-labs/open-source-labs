# カスタムクラスに反復処理機能を追加する

ここでは、ジェネレータの基本を理解したという前提で、カスタムクラスに反復処理機能を追加する方法を学びます。Python でクラスを反復可能（iterable）にするには、`__iter__()` 特殊メソッドを実装する必要があります。反復可能なクラスを使うと、リストやタプルのように、その要素をループで処理することができます。これは非常に強力な機能で、カスタムクラスをより柔軟で使いやすくします。

## `__iter__()` メソッドの理解

`__iter__()` メソッドは、クラスを反復可能にするための重要な部分です。このメソッドはイテレータオブジェクトを返す必要があります。イテレータは、反復処理（ループ）できるオブジェクトです。これを実現する簡単で効果的な方法は、`__iter__()` をジェネレータ関数として定義することです。ジェネレータ関数は `yield` キーワードを使って、値を 1 つずつ生成します。`yield` 文に遭遇するたびに、関数は一時停止し、値を返します。次にイテレータが呼び出されると、関数は中断したところから再開します。

## Structure クラスの修正

この実験のセットアップでは、基本となる `Structure` クラスを用意しています。`Stock` などの他のクラスは、この `Structure` クラスを継承することができます。継承は、既存のクラスのプロパティとメソッドを引き継ぐ新しいクラスを作成する方法です。`Structure` クラスに `__iter__()` メソッドを追加することで、そのすべてのサブクラスを反復可能にすることができます。つまり、`Structure` を継承する任意のクラスは、自動的にループ処理できるようになります。

1. WebIDE で `structure.py` ファイルを開きます。

```bash
cd ~/project
```

このコマンドは、カレントワーキングディレクトリを `project` ディレクトリに変更します。`structure.py` ファイルはこのディレクトリにあります。ファイルにアクセスして変更するには、正しいディレクトリにいる必要があります。

2. `Structure` クラスの現在の実装を見てみましょう。

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

`Structure` クラスには、属性名を格納する `_fields` リストがあります。`__init__()` メソッドはクラスのコンストラクタです。渡された引数の数がフィールドの数と等しいかをチェックして、オブジェクトの属性を初期化します。もし等しくなければ、`TypeError` を発生させます。そうでなければ、`setattr()` 関数を使って属性を設定します。

3. 属性値を順番に生成する `__iter__()` メソッドを追加します。

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

この `__iter__()` メソッドはジェネレータ関数です。`_fields` リストをループし、`getattr()` 関数を使って各属性の値を取得します。そして、`yield` キーワードが値を 1 つずつ返します。

完成した `structure.py` ファイルは次のようになります。

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

この更新された `Structure` クラスには `__iter__()` メソッドがあり、これによりクラス自体とそのサブクラスが反復可能になります。

4. ファイルを保存します。
   `structure.py` ファイルに変更を加えた後は、変更を適用するために保存する必要があります。

5. では、`Stock` インスタンスを作成して反復処理をテストしてみましょう。

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

このコマンドは、`Structure` クラスを継承する `Stock` クラスのインスタンスを作成します。そして、リスト内包表記を使ってインスタンスを反復処理し、各値を出力します。

以下のような出力が表示されるはずです。

```
Iterating over Stock:
GOOG
100
490.1
```

これで、`Structure` を継承する任意のクラスは自動的に反復可能になり、反復処理では `_fields` リストで定義された順序で属性値が生成されます。つまり、`Structure` のサブクラスの属性をループで処理する際に、反復処理用の追加コードを書く必要がなくなります。
