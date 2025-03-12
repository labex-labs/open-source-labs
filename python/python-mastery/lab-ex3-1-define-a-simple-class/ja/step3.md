# ポートフォリオデータの整形と表示

このステップでは、ポートフォリオデータを整然とした表形式で表示する関数を作成します。ポートフォリオは株式の集合であり、このデータを明確かつ読みやすい方法で提示することは重要です。そこで `print_portfolio(portfolio)` 関数が役立ちます。この関数はポートフォリオを入力として受け取り、ヘッダー付きで適切に整列された表形式で表示します。

## Python での文字列整形

Python では、文字列の整形方法が複数あります。文字列整形は、データをより整理された、ユーザーにやさしい方法で提示できるため、重要なスキルです。

- `%` 演算子は古い形式の文字列整形方法です。文字列内の特定の場所に値を挿入できるテンプレートのようなものです。
- `str.format()` メソッドは別の方法です。文字列の整形において、より柔軟性があり、クリーンな構文を提供します。
- f - 文字列は Python 3.6 以降で導入された機能です。文字列リテラル内に式を埋め込むことができるため、非常に便利です。

この演習では `%` 演算子を使用します。固定幅の列を作成する場合に特に便利で、これはポートフォリオ表に必要な機能です。

## 実装手順

1. まず、エディタで `stock.py` ファイルを開きます。すでに開いていれば問題ありません。このファイルに `print_portfolio` 関数を記述します。

2. ファイルを開いたら、`# TODO: Add print_portfolio(portfolio) function here` というコメントを探します。このコメントは、新しい関数を追加する場所を示すマーカーです。

3. そのコメントの下に、次の関数を追加します。

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

この関数はまず表のヘッダー行を表示し、次に区切り線を表示し、最後にポートフォリオ内の各株式をループして、その詳細を整形して表示します。

4. 関数を追加したら、ファイルを保存します。`Ctrl+S` を押すか、メニューから「ファイル > 保存」を選択して保存できます。ファイルを保存することで、変更が保存されます。

5. 次に、関数をテストする必要があります。`test_print.py` という名前の新しいファイルを作成します。このファイルがテストスクリプトになります。以下のコードを追加します。

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

このスクリプトは `stock.py` ファイルから `read_portfolio` と `print_portfolio` 関数をインポートします。次に、CSV ファイルからポートフォリオデータを読み取り、新しく作成した `print_portfolio` 関数を使用して表示します。

6. 最後に、テストスクリプトを実行します。ターミナルを開き、次のコマンドを入力します。

```bash
python3 test_print.py
```

すべてが正しく動作している場合、次のような出力が表示されるはずです。

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

この出力は、`print_portfolio` 関数が期待通りに動作していることを確認します。ヘッダー付きで列が整列された表形式でポートフォリオデータを整形して表示し、読みやすくなっています。

## 文字列整形の理解

`print_portfolio` 関数での文字列整形がどのように機能するかを詳しく見てみましょう。

- `%10s` は文字列の整形に使用されます。`10` はフィールドの幅を示し、`s` は文字列を表します。幅 10 のフィールド内で文字列を右寄せにします。
- `%10d` は整数の整形に使用されます。`10` はフィールドの幅で、`d` は整数を表します。幅 10 のフィールド内で整数を右寄せにします。
- `%10.2f` は浮動小数点数の整形に使用されます。`10` はフィールドの幅で、`.2` は浮動小数点数を小数点以下 2 桁で表示することを指定します。幅 10 のフィールド内で浮動小数点数を右寄せにします。

この整形により、表のすべての列が適切に整列され、出力が読みやすく理解しやすくなります。
