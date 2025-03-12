# 列フォーマットの問題の理解

このステップでは、現在の表フォーマット実装における制限について調べます。また、この問題のいくつかの解決策を検討します。

まず、やることを理解しましょう。VSCode エディタを開き、プロジェクトディレクトリ内の `tableformat.py` ファイルを見ます。このファイルは、表形式のデータをテキスト、CSV、HTML などのさまざまな形式でフォーマットするコードが含まれているため重要です。

ファイルを開くには、ターミナルで以下のコマンドを使用します。`cd` コマンドはディレクトリをプロジェクトディレクトリに変更し、`code` コマンドは VSCode で `tableformat.py` ファイルを開きます。

```bash
cd ~/project
code tableformat.py
```

ファイルを開くと、いくつかのクラスが定義されていることに気づくでしょう。これらのクラスは、表データのフォーマットにおいて異なる役割を果たします。

- `TableFormatter`：これは抽象基底クラス（abstract base class）です。表の見出しと行をフォーマットするためのメソッドがあります。他のフォーマッタクラスの青写真と考えてください。
- `TextTableFormatter`：このクラスは、表を平文形式で出力するために使用されます。
- `CSVTableFormatter`：このクラスは、表データを CSV（Comma-Separated Values）形式でフォーマットする責任があります。
- `HTMLTableFormatter`：このクラスは、表データを HTML 形式でフォーマットします。

また、ファイルには `print_table()` 関数もあります。この関数は、先ほど述べたフォーマッタクラスを使用して表形式のデータを表示します。

では、いくつかの Python コードを実行して、これらのクラスがどのように動作するかを見てみましょう。ターミナルを開き、Python セッションを開始します。以下のコードは、`tableformat.py` ファイルから必要な関数とクラスをインポートし、`TextTableFormatter` オブジェクトを作成し、`print_table()` 関数を使用してポートフォリオデータを表示します。

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

コードを実行すると、以下のような出力が表示されるはずです。

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

では、問題を見つけましょう。`price` 列の値が一貫してフォーマットされていないことに注意してください。一部の値は 32.2 のように小数点以下 1 桁で、他の値は 51.23 のように小数点以下 2 桁です。金融データでは、通常、フォーマットを一貫させたいと思います。

以下は、出力を望む形式です。

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

これを修正する 1 つの方法は、`print_table()` 関数を変更してフォーマット指定を受け取るようにすることです。以下のコードは、これを行う方法を示しています。追加の `formats` パラメータを受け取る新しい `print_table()` 関数を定義します。関数内で、これらのフォーマット指定を使用して行内の各値をフォーマットします。

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

この解決策は機能しますが、欠点があります。関数のインターフェースを変更すると、古いバージョンの `print_table()` 関数を使用している既存のコードが動作しなくなる可能性があります。

別のアプローチは、サブクラス化によってカスタムフォーマッタを作成することです。`TextTableFormatter` を継承する新しいクラスを作成し、`row()` メソッドをオーバーライドして、望むフォーマットを適用することができます。

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

この解決策も機能しますが、あまり便利ではありません。異なるフォーマットが必要になるたびに、新しいクラスを作成する必要があります。また、今回の場合 `TextTableFormatter` からサブクラス化しているため、特定のフォーマッタタイプに制限されます。

次のステップでは、ミックスインクラス（mixin classes）を使用したよりエレガントな解決策を探ります。
