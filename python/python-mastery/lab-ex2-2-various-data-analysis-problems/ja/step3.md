# collections モジュールの探索

Python では、リスト、辞書、セットなどの組み込みコンテナは非常に便利です。しかし、Python の`collections`モジュールは、これらの組み込みコンテナの機能を拡張した特殊なコンテナデータ型を提供することで、さらに一歩進んでいます。これらの便利なデータ型のいくつかを詳しく見てみましょう。

Python ターミナルで作業を続け、以下の例に沿って進めます。

## Counter

`Counter`クラスは辞書のサブクラスです。主な目的は、ハッシュ可能なオブジェクトをカウントすることです。アイテムをカウントする便利な方法を提供し、さまざまな操作をサポートしています。

まず、`Counter`クラスとポートフォリオを読み取る関数をインポートする必要があります。次に、CSV ファイルからポートフォリオを読み取ります。

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

ここで、各株式の名称ごとに株式数をカウントする`Counter`オブジェクトを作成します。

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

`Counter`オブジェクトの素晴らしい特徴の 1 つは、新しいキーを自動的にカウント 0 で初期化することです。これは、カウントを増やす前にキーが存在するかどうかをチェックする必要がなくなるため、カウントを累積するコードを簡素化します。

カウンターには特殊なメソッドもあります。たとえば、`most_common()`メソッドはデータ分析に非常に便利です。

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

さらに、カウンターは算術演算を使って結合することができます。

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

`defaultdict`は通常の辞書に似ていますが、独自の特徴があります。まだ存在しないキーに対してデフォルト値を提供します。これにより、キーを使用する前に存在するかどうかをチェックする必要がなくなるため、コードを簡素化できます。

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

`defaultdict(list)`を作成すると、新しいキーごとに自動的に新しい空のリストが作成されます。したがって、キーが以前に存在しなかった場合でも、直接キーの値に追加することができます。これにより、キーが存在するかどうかをチェックし、手動で空のリストを作成する必要がなくなります。

他のデフォルトファクトリ関数も使用できます。たとえば、`int`、`float`、または独自のカスタム関数を使用することができます。

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

`collections`モジュールのこれらの特殊なコンテナ型は、データを扱う際にコードをより簡潔で効率的にすることができます。
