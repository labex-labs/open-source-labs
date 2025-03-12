# フォーマット用のミックスインクラスの実装

このステップでは、ミックスインクラス（mixin classes）について学びます。ミックスインクラスは Python で非常に便利なテクニックです。これを使うと、クラスの元のコードを変更することなく、追加の機能をクラスに追加できます。これは、コードをモジュール化して管理しやすくするのに役立つため、非常に優れています。

## ミックスインクラスとは何か？

ミックスインは特殊なタイプのクラスです。その主な目的は、他のクラスが継承できる機能を提供することです。ただし、ミックスインは単独で使用することを想定していません。直接ミックスインクラスのインスタンスを作成することはありません。代わりに、特定の機能を他のクラスに制御可能かつ予測可能な方法で追加する手段として使用します。これは多重継承（multiple inheritance）の一種で、クラスが複数の親クラスから継承することができます。

では、`tableformat.py` ファイルに 2 つのミックスインクラスを実装しましょう。まず、エディタでファイルを開きます。ターミナルで以下のコマンドを実行することで、これを行うことができます。

```bash
cd ~/project
code tableformat.py
```

ファイルが開いたら、既存の関数の前で、ファイルの末尾に以下のクラス定義を追加します。

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

この `ColumnFormatMixin` クラスは、列フォーマット機能を提供します。`formats` クラス変数は、フォーマットコードを保持するリストです。これらのコードは、各列のデータをフォーマットするために使用されます。`row()` メソッドは行データを受け取り、行内の各要素にフォーマットコードを適用し、その後 `super().row(rowdata)` を使用してフォーマットされた行データを親クラスに渡します。

次に、表のヘッダーを大文字で表示する別のミックスインクラスを追加します。

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

この `UpperHeadersMixin` クラスは、ヘッダーテキストを大文字に変換します。ヘッダーのリストを受け取り、各ヘッダーを大文字に変換し、その後 `super().headings()` を使用して変更されたヘッダーを親クラスの `headings()` メソッドに渡します。

## ミックスインクラスの使用

新しいミックスインクラスをテストしましょう。いくつかの Python コードを実行して、それらがどのように動作するかを確認します。

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

このコードを実行すると、きれいにフォーマットされた出力が表示されるはずです。`ColumnFormatMixin` が提供するフォーマットにより、価格列は小数点以下の桁数が一致します。

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

では、`UpperHeadersMixin` を試してみましょう。以下のコードを実行します。

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

このコードは、ヘッダーを大文字で表示するはずです。

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## 協調的継承の理解

ミックスインクラスでは、`super().method()` を使用していることに注意してください。これは「協調的継承（cooperative inheritance）」と呼ばれます。協調的継承では、継承チェーン内の各クラスが協力して動作します。クラスが `super().method()` を呼び出すとき、それはチェーン内の次のクラスにタスクの一部を実行するように依頼しています。このように、クラスのチェーンはそれぞれ独自の動作を全体のプロセスに追加することができます。

継承の順序は非常に重要です。`class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)` を定義するとき、Python はまず `ColumnFormatMixin` でメソッドを探し、次に `TextTableFormatter` で探します。したがって、`ColumnFormatMixin` で `super().row()` が呼び出されるとき、それは `TextTableFormatter.row()` を指します。

両方のミックスインを組み合わせることもできます。以下のコードを実行します。

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

このコードは、大文字のヘッダーとフォーマットされた数値の両方を提供します。

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

次のステップでは、`create_formatter()` 関数を拡張することで、これらのミックスインを使いやすくします。
