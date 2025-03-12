# リスト内包表記、セット内包表記、辞書内包表記の使用

Pythonの内包表記は、既存のコレクションに基づいて新しいコレクションを作成する非常に便利で簡潔な方法です。Pythonのコレクションには、リスト、セット、辞書などがあり、これらはさまざまな種類のデータを格納するコンテナのようなものです。内包表記を使うと、特定のデータをフィルタリングしたり、データを何らかの方法で変換したり、より効率的に整理したりすることができます。このセクションでは、ポートフォリオデータを使って、これらの内包表記がどのように機能するかを探ってみましょう。

まず、前のステップと同じようにPythonターミナルを開く必要があります。ターミナルが開いたら、以下の例を1つずつ入力します。この実践的なアプローチにより、内包表記が実際にどのように機能するかを理解するのに役立ちます。

## リスト内包表記

リスト内包表記は、Pythonにおける特殊な構文で、新しいリストを作成します。既存のコレクション内の各アイテムに式を適用することで、これを行います。

例から始めましょう。まず、ポートフォリオデータを読み取る関数をインポートします。次に、リスト内包表記を使って、ポートフォリオから特定の保有株をフィルタリングします。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

このコードでは、まず`read_portfolio`関数をインポートし、CSVファイルからポートフォリオデータを読み取ります。次に、リスト内包表記`[s for s in portfolio if s['shares'] > 100]`が、`portfolio`コレクション内の各アイテム`s`を調べます。保有株数が100を超える場合のみ、そのアイテム`s`を新しいリスト`large_holdings`に含めます。

リスト内包表記は、計算を行うためにも使用できます。いくつかの例を見てみましょう。

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

最初の例では、リスト内包表記`[s['shares'] * s['price'] for s in portfolio]`が、`portfolio`内の各アイテムについて、株式数と価格を掛け合わせて、各保有株の総コストを計算します。2番目の例では、`sum`関数とリスト内包表記を組み合わせて、ポートフォリオ全体の総コストを計算します。

## セット内包表記

セット内包表記は、既存のコレクションからセットを作成するために使用されます。セットは、一意の値のみを含むコレクションです。

ポートフォリオデータでどのように機能するか見てみましょう。

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

このコードでは、セット内包表記`{s['name'] for s in portfolio}`が、`portfolio`内の各アイテム`s`を調べ、株式名 (`s['name']`) をセット`unique_stocks`に追加します。セットは一意の値のみを格納するため、重複のないポートフォリオ内のすべての異なる株式のリストが得られます。

## 辞書内包表記

辞書内包表記は、式を適用してキーと値のペアを作成することで、新しい辞書を作成します。

ポートフォリオ内の各株式の総株式数をカウントするために辞書内包表記を使用する例を見てみましょう。

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

最初の行で、辞書内包表記`{s['name']: 0 for s in portfolio}`が、各株式名 (`s['name']`) をキーとし、各キーの初期値を0とする辞書を作成します。次に、`for`ループを使って`portfolio`内の各アイテムを調べます。各アイテムについて、株式数 (`s['shares']`) を`totals`辞書内の対応する値に加えます。

これらの内包表記は非常に強力で、数行のコードでデータを変換し、分析することができます。Pythonプログラミングのツールボックスには欠かせない便利なツールです。
