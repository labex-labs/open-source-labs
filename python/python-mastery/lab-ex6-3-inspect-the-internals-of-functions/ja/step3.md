# クラスにおける関数検査の適用

ここでは、これまで学んだ関数検査の知識を活用して、クラスの実装を改善します。関数検査を使うと、関数の内部を調べ、その構造（たとえば受け取るパラメータ）を理解することができます。今回は、この機能を使ってクラスのコードをより効率的でエラーが起こりにくいものにします。`Structure` クラスを修正して、`__init__` メソッドのシグネチャから自動的にフィールド名を検出できるようにします。

## Structure クラスの理解

`structure.py` ファイルには `Structure` クラスが含まれています。このクラスは基底クラスとして機能し、他のクラスがこれを継承して構造化されたデータオブジェクトを作成することができます。現在、`Structure` クラスを継承したクラスから作成されるオブジェクトの属性を定義するには、`_fields` クラス変数を設定する必要があります。

エディタでこのファイルを開きましょう。まず、次のコマンドを使ってプロジェクトディレクトリに移動します。

```bash
cd ~/project
```

このコマンドを実行したら、WebIDE 内の `structure.py` ファイルにある既存の `Structure` クラスを見つけて表示することができます。

## Stock クラスの作成

`Structure` クラスを継承した `Stock` クラスを作成しましょう。継承とは、`Stock` クラスが `Structure` クラスのすべての機能を受け取り、さらに独自の機能を追加できることを意味します。`structure.py` ファイルの末尾に次のコードを追加します。

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

しかし、このアプローチには問題があります。`_fields` タプルと `__init__` メソッドの両方を同じパラメータ名で定義する必要があります。これは本質的に同じ情報を 2 回書いているため冗長です。一方を変更したときに他方を更新するのを忘れると、エラーが発生する可能性があります。

## set_fields クラスメソッドの追加

この問題を解決するために、`Structure` クラスに `set_fields` クラスメソッドを追加します。このメソッドは、`__init__` シグネチャから自動的にフィールド名を検出します。`Structure` クラスに追加するコードは次のとおりです。

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

このメソッドは `inspect` モジュールを使用しています。`inspect` モジュールは、関数やクラスなどのオブジェクトに関する情報を取得するための強力なツールです。まず、`__init__` メソッドのシグネチャを取得します。次に、パラメータ名を抽出しますが、`self` パラメータはスキップします。なぜなら、`self` は Python のクラスでインスタンス自体を参照する特別なパラメータだからです。最後に、これらのパラメータ名を使って `_fields` クラス変数を設定します。

## Stock クラスの修正

`set_fields` メソッドができたので、`Stock` クラスを簡素化することができます。前の `Stock` クラスのコードを次のコードに置き換えます。

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

このようにすると、`_fields` タプルを手動で定義する必要がなくなります。`set_fields` メソッドが自動的に処理してくれます。

## 修正後のクラスのテスト

修正したクラスが正しく動作することを確認するために、簡単なテストスクリプトを作成します。`test_structure.py` という新しいファイルを作成し、次のコードを追加します。

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

このテストスクリプトは、`Stock` オブジェクトを作成し、その文字列表現をテストし、属性にアクセスし、属性を変更し、誤ってスペルミスした属性にアクセスして正しいエラーが発生するかを確認します。

テストスクリプトを実行するには、次のコマンドを使用します。

```bash
python3 test_structure.py
```

次のような出力が表示されるはずです。

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## 動作原理

1. `set_fields` メソッドは `inspect.signature()` を使って `__init__` メソッドのパラメータ名を取得します。この関数は、`__init__` メソッドのパラメータに関する詳細な情報を提供します。
2. その後、これらのパラメータ名に基づいて `_fields` クラス変数を自動的に設定します。これにより、同じパラメータ名を 2 つの異なる場所に書く必要がなくなります。
3. これにより、`_fields` と `__init__` を一致するパラメータ名で手動で定義する必要がなくなります。`__init__` メソッドのパラメータを変更した場合、`_fields` も自動的に更新されるため、コードの保守性が向上します。

このアプローチは、関数検査を使ってコードをより保守しやすく、エラーが起こりにくいものにします。これは、Python のイントロスペクション機能を実際に応用したもので、実行時にオブジェクトを調べたり変更したりすることができます。
