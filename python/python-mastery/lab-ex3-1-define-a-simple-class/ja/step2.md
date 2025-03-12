# CSV ファイルからポートフォリオを読み取る

このステップでは、CSV ファイルから株式データを読み取り、`Stock` オブジェクトのリストを返す関数を作成します。`Stock` オブジェクトは株式保有を表し、このステップの最後までに、CSV ファイルから株式ポートフォリオを読み取ることができるようになります。

## CSV ファイルの理解

CSV は Comma-Separated Values の略で、表形式のデータを保存するための非常に一般的な形式です。簡単なスプレッドシートのようなものと考えてください。CSV ファイルの各行はデータの行を表し、その行内の列はコンマで区切られています。通常、CSV ファイルの最初の行にはヘッダーが含まれています。これらのヘッダーは、各列にどのようなデータが含まれているかを説明します。たとえば、株式ポートフォリオの CSV では、ヘッダーは「Name」、「Shares」、「Price」になるかもしれません。

## 実装手順

1. まず、コードエディタで `stock.py` ファイルを開きます。すでに開いていれば問題ありません。開いていない場合は、それを見つけて開きます。ここに新しい関数を追加します。

2. `stock.py` ファイルが開いたら、`# TODO: Add read_portfolio(filename) function here` というコメントを探します。このコメントは、新しい関数を配置する場所を示すプレースホルダーです。

3. そのコメントの下に、次の関数を追加します。この関数は `read_portfolio` と呼ばれ、ファイル名を引数として受け取ります。この関数の目的は、CSV ファイルを読み取り、株式データを抽出し、`Stock` オブジェクトのリストを作成することです。

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

この関数が何をするかを分解してみましょう。まず、`portfolio` という空のリストを作成します。次に、CSV ファイルを読み取りモードで開きます。`next(f)` 文は最初の行（ヘッダー行）をスキップします。その後、ファイルの各行をループします。各行について、その行を値のリストに分割し、名前、株式数、価格を抽出し、`Stock` オブジェクトを作成し、`portfolio` リストに追加します。最後に、`portfolio` リストを返します。

4. 関数を追加したら、`stock.py` ファイルを保存します。キーボードで `Ctrl+S` を押すか、コードエディタのメニューから「ファイル > 保存」を選択して保存できます。ファイルを保存することで、変更が保存されます。

5. 次に、`read_portfolio` 関数をテストする必要があります。`test_portfolio.py` という名前の新しい Python スクリプトを作成します。このスクリプトは `stock.py` ファイルから `read_portfolio` 関数をインポートし、CSV ファイルからポートフォリオを読み取り、ポートフォリオ内の各株式に関する情報を印刷します。

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

このスクリプトでは、まず `read_portfolio` 関数をインポートします。次に、ファイル名 `portfolio.csv` を指定して関数を呼び出し、`Stock` オブジェクトのリストを取得します。その後、リストをループして各株式に関する情報を印刷します。最後に、ポートフォリオ内の株式の総数を印刷します。

6. テストスクリプトを実行するには、ターミナルまたはコマンドプロンプトを開き、`test_portfolio.py` ファイルがあるディレクトリに移動して、次のコマンドを実行します。

```bash
python3 test_portfolio.py
```

すべてが正しく動作している場合、`portfolio.csv` ファイル内のすべての株式の名前、株式数、価格が一覧表示された出力が表示されるはずです。また、ポートフォリオ内の株式の総数も表示されます。

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

この出力は、`read_portfolio` 関数が CSV ファイルを正しく読み取り、そのデータから `Stock` オブジェクトを作成していることを確認します。
