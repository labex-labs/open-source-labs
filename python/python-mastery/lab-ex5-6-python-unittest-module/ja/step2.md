# テストケースの拡張

基本的なテストケースを作成したので、次はテストの範囲を拡大しましょう。さらに多くのテストを追加することで、`Stock` クラスの残りの機能を網羅することができます。これにより、クラスのすべての側面が期待どおりに動作することを保証できます。`TestStock` クラスを修正して、いくつかのメソッドとプロパティのテストを追加します。

1. `teststock.py` ファイルを開きます。`TestStock` クラスの中に、いくつかの新しいテストメソッドを追加します。これらのメソッドは、`Stock` クラスの異なる部分をテストします。追加する必要のあるコードは次のとおりです。

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

これらの各テストが何を行っているか、もう少し詳しく見てみましょう。

- `test_create_keyword_args`: このテストは、キーワード引数を使用して `Stock` オブジェクトを作成できるかどうかをチェックします。オブジェクトの属性が正しく設定されていることを検証します。
- `test_cost`: このテストは、`Stock` オブジェクトの `cost` プロパティが正しい値を返すかどうかをチェックします。この値は、株式数に価格を掛けたものとして計算されます。
- `test_sell`: このテストは、`Stock` オブジェクトの `sell()` メソッドが一部の株式を売却した後に株式数を正しく更新するかどうかをチェックします。
- `test_from_row`: このテストは、`from_row()` クラスメソッドがデータ行から新しい `Stock` インスタンスを作成できるかどうかをチェックします。
- `test_repr`: このテストは、`Stock` オブジェクトの `__repr__()` メソッドが期待される文字列表現を返すかどうかをチェックします。
- `test_eq`: このテストは、`__eq__()` メソッドが 2 つの `Stock` オブジェクトを正しく比較して等しいかどうかを判断できるかどうかをチェックします。

2. これらのテストメソッドを追加したら、`teststock.py` ファイルを保存します。次に、ターミナルで以下のコマンドを使用してテストを再度実行します。

```bash
python3 teststock.py
```

すべてのテストが合格した場合、次のような出力が表示されるはずです。

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

出力の 7 つのドットは、それぞれのテストを表しています。各ドットは、テストが正常に通過したことを示します。したがって、7 つのドットが表示された場合は、7 つのテストすべてが合格したことを意味します。
