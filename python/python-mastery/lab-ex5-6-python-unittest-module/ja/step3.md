# 例外のテスト

テストはソフトウェア開発の重要な部分であり、その重要な側面の 1 つは、コードがエラー状況を適切に処理できることを保証することです。Python では、`unittest` モジュールが特定の例外が期待通りに発生するかどうかをテストする便利な方法を提供しています。

1. `teststock.py` ファイルを開きます。例外をチェックするためのテストメソッドを追加します。これらのテストは、無効な入力に遭遇したときにコードが正しく動作することを確認するのに役立ちます。

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

これらの例外テストがどのように動作するかを理解しましょう。

- `with self.assertRaises(ExceptionType):` 文はコンテキストマネージャを作成します。このコンテキストマネージャは、`with` ブロック内のコードが指定された例外を発生させるかどうかをチェックします。
- `with` ブロック内で期待される例外が発生した場合、テストは合格します。これは、コードが無効な入力を正しく検出し、適切なエラーを発生させていることを意味します。
- 例外が発生しないか、異なる例外が発生した場合、テストは失敗します。これは、コードが無効な入力を期待通りに処理していない可能性があることを示しています。

これらのテストは、以下のシナリオを検証するように設計されています。

- `shares` 属性を文字列に設定すると、`shares` は数値である必要があるため、`TypeError` が発生するはずです。
- `shares` 属性を負の数に設定すると、株式数は負にすることができないため、`ValueError` が発生するはずです。
- `price` 属性を文字列に設定すると、`price` は数値である必要があるため、`TypeError` が発生するはずです。
- `price` 属性を負の数に設定すると、価格は負にすることができないため、`ValueError` が発生するはずです。
- 存在しない属性 `share`（末尾の 's' が欠けている）を設定しようとすると、正しい属性名は `shares` であるため、`AttributeError` が発生するはずです。

2. これらのテストメソッドを追加したら、`teststock.py` ファイルを保存します。次に、ターミナルで以下のコマンドを使用してすべてのテストを実行します。

```bash
python3 teststock.py
```

すべてが正しく動作している場合、12 のテストすべてが合格したことを示す出力が表示されるはずです。出力は次のようになります。

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

12 個のドットは、これまでに書いたすべてのテストを表しています。前のステップで 7 つのテストがあり、ここで 5 つの新しいテストを追加しました。この出力は、コードが例外を期待通りに処理していることを示しており、十分にテストされたプログラムの良い兆しです。
