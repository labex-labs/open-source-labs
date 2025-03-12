# 実装のテスト

メタクラスを実装し、`Structure` クラスを変更したので、実装のテストを行う時が来ました。テストは、すべてが正しく動作していることを確認するのに役立つため、非常に重要です。テストを実行することで、潜在的な問題を早期に発見し、コードが期待通りに動作することを確認できます。

まず、`Stock` クラスが期待通りに動作するかどうかを確認するために、単体テストを実行しましょう。単体テストは、コードの個々の部分をチェックする小さな独立したテストです。この場合、`Stock` クラスが正しく機能することを確認したいと思います。単体テストを実行するには、ターミナルで次のコマンドを使用します。

```bash
python3 teststock.py
```

すべてが正しく動作している場合、すべてのテストがエラーなくパスするはずです。テストが正常に実行されると、出力は次のようになります。

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

ドットはパスした各テストを表し、最後の `OK` はすべてのテストが成功したことを示します。

では、実際のデータとテーブル整形機能を使用して `Stock` クラスをテストしましょう。これにより、`Stock` クラスがデータとどのように相互作用するか、およびテーブル整形がどのように機能するかを、より現実的なシナリオで確認できます。ターミナルで次のコマンドを使用します。

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

このコードでは、まず必要なクラスと関数をインポートします。次に、CSV ファイルからのデータを `Stock` インスタンスに読み込みます。その後、ポートフォリオデータを印刷し、テーブルに整形して整形されたテーブルを印刷します。

次のような出力が表示されるはずです。

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
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

私たちが達成したことを振り返ってみましょう。

1. すべてのバリデータ型を自動的に収集するメカニズムを作成しました。これは、すべてのバリデータを手動で追跡する必要がないことを意味し、時間を節約し、エラーの可能性を減らします。
2. これらの型を `Structure` サブクラスの名前空間に注入するメタクラスを実装しました。これにより、サブクラスはこれらのバリデータを明示的にインポートすることなく使用できます。
3. バリデータ型の明示的なインポートの必要性を排除しました。これにより、コードがよりクリーンで読みやすくなります。
4. これらすべての処理は裏で行われるため、新しい構造を定義するコードがクリーンでシンプルになります。

最終的な `stock.py` ファイルは、メタクラスを使用しない場合と比較して非常にクリーンです。

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

バリデータ型を直接インポートする必要がないため、コードはより簡潔で保守しやすくなります。これは、メタクラスがコードの品質を向上させることができる素晴らしい例です。
