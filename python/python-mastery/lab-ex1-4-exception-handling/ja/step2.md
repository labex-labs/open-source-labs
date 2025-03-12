# エラーハンドリングの追加

実際のデータを扱う際には、データの不整合やエラーに遭遇することが非常に一般的です。たとえば、データに欠損値があったり、形式が正しくなかったり、その他の問題があることがあります。Python では、このような状況を適切に処理するための例外処理メカニズムが用意されています。例外処理を使用すると、プログラムがエラーに遭遇しても突然クラッシュすることなく、実行を続けることができます。

## 問題の理解

`portfolio3.dat` ファイルを見てみましょう。このファイルには、株式シンボル、株数、1 株あたりの価格など、ポートフォリオに関するデータが含まれています。このファイルの内容を表示するには、次のコマンドを使用できます。

```bash
cat /home/labex/project/portfolio3.dat
```

このコマンドを実行すると、ファイル内の一部の行では、株数の部分に数字の代わりにダッシュ (`-`) が使われていることに気づくでしょう。以下は、見られる内容の例です。

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

現在のコードをこのファイルに対して実行しようとすると、プログラムはクラッシュします。その理由は、コードが株数を整数に変換しようとするのに、ダッシュ (`-`) を整数に変換することができないからです。コードを実行して、何が起こるか見てみましょう。

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

次のようなエラーメッセージが表示されるでしょう。

```
ValueError: invalid literal for int() with base 10: '-'
```

このエラーは、Python が `int(fields[1])` を実行しようとして `-` 文字を整数に変換できないときに発生します。

## 例外処理の紹介

Python の例外処理では、`try` ブロックと `except` ブロックが使用されます。`try` ブロックには、例外を引き起こす可能性のあるコードが含まれています。例外とは、プログラムの実行中に発生するエラーのことです。`except` ブロックには、`try` ブロック内で例外が発生した場合に実行されるコードが含まれています。

以下は、`try` ブロックと `except` ブロックがどのように動作するかの例です。

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

Python が `try` ブロック内のコードを実行するときに例外が発生すると、実行はすぐに一致する `except` ブロックにジャンプします。`except` ブロック内の `ExceptionType` は、処理したい例外のタイプを指定します。変数 `e` には、エラーメッセージなど、例外に関する情報が含まれています。

## 例外処理を用いた関数の修正

`pcost.py` ファイルを更新して、データ内のエラーを処理できるようにしましょう。`try` ブロックと `except` ブロックを使用して、不適切なデータが含まれる行をスキップし、警告メッセージを表示します。

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    Handles lines with bad data by skipping them and showing a warning.

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # Extract the data (symbol, shares, price)
                shares = int(fields[1])
                price = float(fields[2])
                # Add the cost to our running total
                total_cost += shares * price
            except ValueError as e:
                # Print a warning for lines that can't be parsed
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Call the function with the portfolio3.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

この更新されたコードでは、まずファイルを開き、1 行ずつ読み取ります。各行について、フィールドに分割します。そして、株数を整数に、価格を浮動小数点数に変換しようとします。この変換が失敗した場合（つまり、`ValueError` が発生した場合）、警告メッセージを表示し、その行をスキップします。そうでない場合は、株式のコストを計算し、総コストに加算します。

## 更新された関数のテスト

では、問題のあるファイルで更新されたプログラムを実行してみましょう。まず、プロジェクトディレクトリに移動し、Python スクリプトを実行します。

```bash
cd /home/labex/project
python3 pcost.py
```

次のような出力が表示されるはずです。

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

このプログラムは現在、以下のことを行います。

1. ファイルの各行を処理しようとします。
2. 行に無効なデータが含まれている場合、`ValueError` を捕捉します。
3. 問題に関する有益なメッセージを表示します。
4. ファイルの残りの部分の処理を続けます。
5. 有効な行に基づいて総コストを返します。

このアプローチにより、不完全なデータを扱う際にプログラムがはるかに堅牢になります。エラーを適切に処理し、依然として有用な結果を提供することができます。
