# 継承を用いた検証システムの構築

このステップでは、継承を使って実用的な検証システムを構築します。継承はプログラミングにおける強力な概念で、既存のクラスを基に新しいクラスを作成することができます。これにより、コードを再利用し、より組織的でモジュール化されたプログラムを作成することができます。この検証システムを構築することで、継承を使ってさまざまな方法で組み合わせることができる再利用可能なコードコンポーネントを作成する方法を学びます。

## 基本検証クラスの作成

まず、検証器の基本クラスを作成する必要があります。これを行うには、WebIDEで新しいファイルを作成します。以下のように操作します。「File」>「New File」をクリックするか、キーボードショートカットを使用します。新しいファイルが開いたら、`validate.py`と名付けます。

では、このファイルにコードを追加して、基本の`Validator`クラスを作成しましょう。このクラスは、他のすべての検証器の基礎となります。

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

このコードでは、`check`メソッドを持つ`Validator`クラスを定義しています。`check`メソッドは値を引数として受け取り、その値をそのまま返します。`@classmethod`デコレータは、このメソッドをクラスメソッドにするために使用されています。これは、クラスのインスタンスを作成することなく、クラス自体でこのメソッドを呼び出すことができることを意味します。

## 型検証器の追加

次に、値の型をチェックする検証器を追加します。これらの検証器は、先ほど作成した`Validator`クラスを継承します。`validate.py`ファイルに戻り、以下のコードを追加します。

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

`Typed`クラスは`Validator`のサブクラスです。`expected_type`属性を持ち、初期値は`object`に設定されています。`Typed`クラスの`check`メソッドは、与えられた値が期待される型であるかをチェックします。もしそうでなければ、`TypeError`を発生させます。型が正しければ、`super().check(value)`を使って親クラスの`check`メソッドを呼び出します。

`Integer`、`Float`、`String`クラスは`Typed`を継承し、チェックする正確な型を指定しています。たとえば、`Integer`クラスは値が整数であるかをチェックします。

## 型検証器のテスト

型検証器を作成したので、テストしてみましょう。新しいターミナルを開き、以下のコマンドを実行してPythonインタープリタを起動します。

```bash
python3
```

Pythonインタープリタが起動したら、検証器をインポートしてテストすることができます。以下のコードでテストします。

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

このコードを実行すると、以下のような出力が表示されるはずです。

```
10
Error: Expected <class 'int'>
'10'
```

これらの検証器を関数内で使用することもできます。試してみましょう。

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

このコードを実行すると、以下のような出力が表示されるはずです。

```
4
Error: Expected <class 'int'>
```

## 値検証器の追加

これまで、値の型をチェックする検証器を作成しました。次に、型ではなく値自体をチェックする検証器を追加しましょう。`validate.py`ファイルに戻り、以下のコードを追加します。

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

`Positive`検証器は、値が非負であるかをチェックします。値が0未満の場合、`ValueError`を発生させます。`NonEmpty`検証器は、値の長さがゼロでないかをチェックします。長さが0の場合、`ValueError`を発生させます。

## 多重継承による検証器の組み合わせ

次に、多重継承を使って検証器を組み合わせます。多重継承により、クラスは複数の親クラスから継承することができます。`validate.py`ファイルに戻り、以下のコードを追加します。

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

これらの新しいクラスは、型チェックと値チェックを組み合わせています。たとえば、`PositiveInteger`クラスは、値が整数であり、かつ非負であることをチェックします。ここでは継承の順序が重要です。検証器は、クラス定義で指定された順序でチェックされます。

## 組み合わせた検証器のテスト

組み合わせた検証器をテストしてみましょう。Pythonインタープリタで以下のコードを実行します。

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

このコードを実行すると、以下のような出力が表示されるはずです。

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

これは、検証器を組み合わせてより複雑な検証ルールを作成する方法を示しています。

テストが終了したら、以下のコマンドを実行してPythonインタープリタを終了することができます。

```python
exit()
```
