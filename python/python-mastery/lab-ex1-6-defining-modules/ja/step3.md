# 独自のモジュールの作成

既存のモジュールの使い方がわかったところで、新しいモジュールをゼロから作成しましょう。Python のモジュールは、Python の定義や文を含むファイルです。これにより、コードを再利用可能で管理しやすいピースに整理することができます。独自のモジュールを作成することで、関連する関数や変数をまとめることができ、コードをよりモジュール化し、メンテナンスしやすくすることができます。

## レポートモジュールの作成

株式レポートを生成するための簡単なモジュールを作成しましょう。このモジュールには、ポートフォリオファイルを読み込み、ポートフォリオ内の株式の整形されたレポートを印刷する関数が含まれます。

1. まず、`report.py` という名前の新しいファイルを作成する必要があります。これを行うには、コマンドラインを使用します。ホームディレクトリ内の `project` ディレクトリに移動し、`touch` コマンドを使用してファイルを作成します。

```bash
cd ~/project
touch report.py
```

2. 次に、好みのテキストエディタで `report.py` ファイルを開き、以下のコードを追加します。このコードは 2 つの関数とメインブロックを定義しています。

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

`read_portfolio` 関数は、株式情報を含むファイルを読み込み、辞書のリストを返します。各辞書は、`name`、`shares`、`price` をキーとする株式を表します。`print_report` 関数は、ポートフォリオ（株式辞書のリスト）を受け取り、株式名、株数、価格、および総価値を示す整形されたレポートを印刷します。末尾のメインブロックは、ファイルが直接実行されたときに実行されます。ポートフォリオファイルを読み込み、レポートを印刷します。

3. コードを追加した後、ファイルを保存してエディタを終了します。

## モジュールのテスト

新しいモジュールが期待通りに動作することを確認するために、テストを行いましょう。

1. まず、コマンドラインからスクリプトを直接実行します。これにより、`report.py` ファイル内のメインブロックが実行されます。

```bash
python3 report.py
```

ポートフォリオ内の株式とその価値を示す整形されたレポートが表示されるはずです。このレポートには、株式名、株数、価格、総価値、およびポートフォリオ全体の総価値が含まれます。

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. 次に、Python インタープリターからモジュールを使用します。ターミナルで `python3` コマンドを実行して、Python インタープリターを起動します。

```bash
python3
```

インタープリターが起動したら、`report` モジュールをインポートし、その関数を使用することができます。

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

`import report` 文により、`report.py` ファイルで定義された関数や変数が現在の Python セッションで使用可能になります。次に、`read_portfolio` 関数を使用してポートフォリオファイルを読み込み、結果を `portfolio` 変数に格納します。`len(portfolio)` 文はポートフォリオ内の株式の数を返し、`portfolio[0]` はポートフォリオ内の最初の株式を返します。

以下の出力が表示されるはずです。

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. では、インポートしたモジュールを使用して、自分でポートフォリオの総コストを計算しましょう。ポートフォリオ内の株式を繰り返し処理し、各株式の総価値を合計します。

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

出力は `44671.15` であるはずで、これは `print_report` 関数によって印刷される総価値と同じです。

4. 最後に、特定の株式タイプに対するカスタムレポートを作成しましょう。ポートフォリオをフィルタリングして、IBM の株式のみを含め、`print_report` 関数を使用してそれらの株式のレポートを印刷します。

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

これにより、IBM の株式とその価値のみを示すレポートが印刷されるはずです。

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. テストが終了したら、`exit()` コマンドを実行して Python インタープリターを終了します。

```python
exit()
```

これで、独自の Python モジュールを作成し、使用することに成功しました。関数と、ファイルが直接実行されたときにのみ実行されるメインブロックの両方を組み合わせています。このようなモジュール化されたプログラミングアプローチにより、コードを再利用し、プロジェクトをより整理された状態でメンテナンスしやすくすることができます。
