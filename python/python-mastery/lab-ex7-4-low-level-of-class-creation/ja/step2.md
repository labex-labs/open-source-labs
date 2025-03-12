# 型付き構造ヘルパーの作成

このステップでは、より実用的な例を構築します。型検証を行うクラスを作成する関数を実装します。型検証は、クラス属性に割り当てられるデータが特定の基準（特定のデータ型や特定の範囲内であるなど）を満たすことを保証するため、非常に重要です。これにより、エラーを早期に発見でき、コードをより堅牢にすることができます。

## Structure クラスの理解

まず、WebIDE エディタで `structure.py` ファイルを開く必要があります。このファイルには基本的な `Structure` クラスが含まれています。このクラスは、構造化されたオブジェクトの初期化と表現の基本的な機能を提供します。初期化とは、提供されたデータでオブジェクトをセットアップすることを意味し、表現とは、オブジェクトを印刷したときにどのように表示されるかを指します。

ファイルを開くには、ターミナルで以下のコマンドを使用します。

```bash
cd ~/project
```

このコマンドを実行すると、`structure.py` ファイルがある正しいディレクトリに移動します。ファイルを開くと、基本的な `Structure` クラスが表示されます。我々の目標は、このクラスを拡張して型検証をサポートすることです。

## typed_structure 関数の実装

では、`structure.py` ファイルに `typed_structure` 関数を追加しましょう。この関数は、`Structure` クラスを継承し、指定されたバリデータ（検証器）を含む新しいクラスを作成します。継承とは、新しいクラスが `Structure` クラスのすべての機能を持ち、独自の機能も追加できることを意味します。バリデータは、クラス属性に割り当てられた値が有効かどうかをチェックするために使用されます。

以下は `typed_structure` 関数のコードです。

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

`clsname` パラメータは、新しいクラスに付けたい名前です。`validators` パラメータは、キーが属性名で、値がバリデータオブジェクトである辞書です。`type()` 関数は、新しいクラスを動的に作成するために使用されます。この関数は 3 つの引数を取ります。クラス名、基底クラスのタプル（この場合は `Structure` クラスのみ）、およびクラス属性の辞書（バリデータ）です。

この関数を追加した後、`structure.py` ファイルは次のようになるはずです。

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## typed_structure 関数のテスト

`validate.py` ファイルのバリデータを使用して、`typed_structure` 関数をテストしましょう。これらのバリデータは、クラス属性に割り当てられた値が正しい型であり、他の基準を満たしているかどうかをチェックするために使用されます。

まず、Python インタラクティブシェルを開きます。ターミナルで以下のコマンドを使用します。

```bash
cd ~/project
python3
```

最初のコマンドで正しいディレクトリに移動し、2 番目のコマンドで Python インタラクティブシェルを起動します。

必要なコンポーネントをインポートし、型付き構造を作成します。

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

`validate.py` ファイルから `String`、`PositiveInteger`、`PositiveFloat` バリデータをインポートします。次に、`typed_structure` 関数を使用して、型検証付きの `Stock` クラスを作成します。`Stock` クラスのインスタンスを作成し、その属性を印刷することでテストします。最後に、無効な株式インスタンスを作成して検証をテストします。

以下のような出力が表示されるはずです。

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

テストが終了したら、Python シェルを終了します。

```python
exit()
```

この例は、`type()` 関数を使用して特定の検証ルールを持つカスタムクラスを作成する方法を示しています。このアプローチは非常に強力で、クラスをプログラムで生成できるため、多くの時間を節約し、コードをより柔軟にすることができます。
