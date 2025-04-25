# getattr() を使用した汎用的なオブジェクト処理

`getattr()` 関数は、Python においてオブジェクトの属性に動的にアクセスできる強力なツールです。これは、オブジェクトを汎用的に処理したい場合に特に便利です。特定のオブジェクト型に特化したコードを書く代わりに、`getattr()` を使用して、必要な属性を持つ任意のオブジェクトを扱うことができます。この柔軟性により、コードの再利用性と適応性が向上します。

## 複数の属性の処理

まず、`getattr()` 関数を使用してオブジェクトの複数の属性にアクセスする方法を学びましょう。これは、オブジェクトから特定の情報を抽出する必要がある一般的なシナリオです。

前の Python 対話型シェルを閉じた場合は、新しく開きましょう。ターミナルで以下のコマンドを実行することで、対話型シェルを開くことができます。

```python
# Open a Python interactive shell if you closed the previous one
python3
```

次に、`Stock` クラスをインポートし、`Stock` オブジェクトを作成します。`Stock` クラスは、`name`、`shares`、`price` などの属性を持つ株式を表します。

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

ここで、アクセスしたい属性名のリストを定義します。このリストを使って属性を繰り返し処理し、その値を表示します。

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

最後に、`for` ループを使用して属性名のリストを繰り返し処理し、`getattr()` を使用して各属性にアクセスします。各繰り返しで属性名とその値を表示します。

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

このコードを実行すると、以下の出力が表示されます。

```
name: GOOG
shares: 100
price: 490.1
```

この出力は、`getattr()` 関数を使用して `Stock` オブジェクトの複数の属性の値にアクセスし、表示できたことを示しています。

## getattr() でのデフォルト値

`getattr()` 関数には、アクセスしようとする属性が存在しない場合にデフォルト値を指定できる便利な機能もあります。これにより、コードが `AttributeError` を発生させるのを防ぎ、より堅牢にすることができます。

これがどのように機能するか見てみましょう。まず、`Stock` オブジェクトに存在しない属性にアクセスしてみます。`getattr()` を使用し、デフォルト値として `'N/A'` を指定します。

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

この場合、`Stock` オブジェクトに `symbol` 属性が存在しないため、`getattr()` はデフォルト値 `'N/A'` を返します。

次に、存在する属性にアクセスする場合と比較してみましょう。`Stock` オブジェクトに存在する `name` 属性にアクセスします。

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

ここでは、`getattr()` は `name` 属性の実際の値である `'GOOG'` を返します。

## オブジェクトのコレクションの処理

`getattr()` 関数は、オブジェクトのコレクションを処理する必要がある場合にさらに強力になります。株式ポートフォリオを処理するためにこれをどのように使用できるか見てみましょう。

まず、`stock` モジュールから `read_portfolio` 関数をインポートします。この関数は、CSV ファイルから株式ポートフォリオを読み込み、`Stock` オブジェクトのリストを返します。

```python
# Import the portfolio reading function
from stock import read_portfolio
```

次に、`read_portfolio` 関数を使用して、`portfolio.csv` という名前の CSV ファイルからポートフォリオを読み込みます。

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

最後に、`for` ループを使用して、ポートフォリオ内の `Stock` オブジェクトのリストを繰り返し処理します。各株式について、`getattr()` を使用して `name` と `shares` 属性にアクセスし、その値を表示します。

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

このアプローチは、属性名を文字列として扱うことができるため、コードをより柔軟にします。これらの文字列は引数として渡したり、データ構造に格納したりすることができるため、コードの核心ロジックを変更することなく、アクセスしたい属性を簡単に変更できます。
