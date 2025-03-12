# 抽象基底クラスの実装

このステップでは、Python の `abc` モジュールを使用して、`TableFormatter` クラスを適切な抽象基底クラス (ABC) に変換します。まずは、抽象基底クラスとは何か、なぜ必要なのかを理解しましょう。

## 抽象基底クラスの理解

抽象基底クラスは、Python の特殊なクラスです。直接オブジェクトを作成することができないクラスで、つまりインスタンス化することができません。抽象基底クラスの主な目的は、サブクラスに共通のインターフェースを定義することです。すべてのサブクラスが従わなければならない一連のルールを設定します。具体的には、サブクラスに特定のメソッドを実装することを要求します。

抽象基底クラスに関するいくつかの重要な概念を紹介します。

- Python では `abc` モジュールを使用して抽象基底クラスを作成します。
- `@abstractmethod` デコレータでマークされたメソッドはルールのようなものです。抽象基底クラスを継承するすべてのサブクラスは、これらのメソッドを実装しなければなりません。
- 抽象基底クラスを継承しているが、すべての必要なメソッドを実装していないクラスのオブジェクトを作成しようとすると、Python はエラーを発生させます。

抽象基底クラスの基本を理解したので、`TableFormatter` クラスを抽象基底クラスに変更する方法を見てみましょう。

## TableFormatter クラスの修正

`tableformat.py` ファイルを開きます。`TableFormatter` クラスを変更して、`abc` モジュールを使用し、抽象基底クラスにします。

1. まず、`abc` モジュールから必要なものをインポートする必要があります。ファイルの先頭に次のインポート文を追加します。

```python
# tableformat.py
from abc import ABC, abstractmethod
```

このインポート文は、2 つの重要なものを持ってきます。`ABC` は Python のすべての抽象基底クラスの基底クラスで、`abstractmethod` はメソッドを抽象メソッドとしてマークするために使用するデコレータです。

2. 次に、`TableFormatter` クラスを修正します。抽象基底クラスにするために `ABC` を継承し、`@abstractmethod` デコレータを使用してそのメソッドを抽象メソッドとしてマークします。修正後のクラスは次のようになります。

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

この修正されたクラスについていくつか注意点があります。

- クラスは現在 `ABC` を継承しており、これは公式に抽象基底クラスであることを意味します。
- `headings` メソッドと `row` メソッドの両方が `@abstractmethod` でデコレートされています。これは、`TableFormatter` のサブクラスがこれらのメソッドを実装しなければならないことを Python に伝えます。
- `NotImplementedError` を `pass` に置き換えました。`@abstractmethod` デコレータがサブクラスがこれらのメソッドを実装することを保証するので、もはや `NotImplementedError` は必要ありません。

## 抽象基底クラスのテスト

`TableFormatter` クラスを抽象基底クラスにしたので、正しく動作するかテストしましょう。次のコードを持つ `test_abc.py` というファイルを作成します。

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

このコードには 2 つのテストケースがあります。最初のテストケースでは、`TableFormatter` を継承しようとするが、メソッド名が誤っている `NewFormatter` クラスを定義しています。2 番目のテストケースでは、すべての必要なメソッドを正しく実装した `ProperFormatter` クラスを定義しています。

テストを実行するには、ターミナルを開き、次のコマンドを実行します。

```bash
python test_abc.py
```

次のような出力が表示されるはずです。

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

この出力は、抽象基底クラスが期待どおりに動作していることを確認します。最初のテストケースは、`NewFormatter` クラスが `headings` メソッドを正しく実装していなかったために失敗します。2 番目のテストケースは、`ProperFormatter` クラスがすべての必要なメソッドを実装していたために成功します。
