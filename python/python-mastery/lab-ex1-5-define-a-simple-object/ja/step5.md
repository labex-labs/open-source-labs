# 株式クラスの機能拡張

Python において、クラスはデータと振る舞いを整理する強力な手段です。関連するデータと関数をまとめることができます。このセクションでは、フォーマットされた株式情報を表示するメソッドを追加することで、`Stock` クラスを拡張します。これは、データと振る舞いの両方をクラスにカプセル化できる素晴らしい例です。カプセル化とは、データとそのデータを操作するメソッドをまとめることで、コードを整理し、管理しやすくすることを意味します。

1. まず、WebIDE のエディタで `stock.py` ファイルを開く必要があります。`stock.py` ファイルは、`Stock` クラスを開発してきた場所です。エディタで開くことで、クラス定義に変更を加えることができます。

2. 次に、`Stock` クラスを修正して、新しい `display()` メソッドを追加します。このメソッドは、株式情報を見やすくフォーマットして出力する役割を担います。以下のように実装できます。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

`__init__` メソッドでは、株式の名前、株数、価格を初期化します。`cost` メソッドは、株数に価格を掛けることで株式の総コストを計算します。新しい `display` メソッドは、f - 文字列を使用して、株式の名前、株数、価格、総コストを含む株式情報をフォーマットして出力します。

3. これらの変更を加えた後、ファイルを保存する必要があります。キーボードで `Ctrl+S` を押すか、エディタの保存アイコンをクリックすることで保存できます。ファイルを保存することで、変更が保存され、後で使用できるようになります。

4. 次に、新しい Python の対話セッションを開始します。対話セッションを使うと、すぐにコードをテストすることができます。セッションを開始するには、ターミナルで以下のコマンドを実行します。

```bash
python3 -i stock.py
```

`-i` オプションは、Python に `stock.py` ファイルを実行した後に対話セッションを開始するよう指示します。これにより、すぐに `Stock` クラスとそのメソッドを使用することができます。

5. では、株式オブジェクトを作成し、新しい `display()` メソッドを使用してみましょう。Apple の株式を表すオブジェクトを作成し、`display` メソッドを呼び出して、フォーマットされた情報を確認します。以下がコードです。

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

このコードを対話セッションで実行すると、以下の出力が表示されます。

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

この出力は、`display` メソッドが正しく動作し、株式情報を期待通りにフォーマットしていることを示しています。

6. 最後に、株式のリストを作成し、すべての株式情報を表示しましょう。これにより、複数の株式オブジェクトで `display` メソッドを使用できることがわかります。以下がコードです。

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

このコードを実行すると、以下の出力が得られます。

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

`display()` メソッドをクラスに追加することで、フォーマットロジックをクラス自体にカプセル化しました。これにより、コードがより整理され、保守が容易になります。株式情報の表示方法を変更する必要がある場合、コード全体に変更を加えるのではなく、`display` メソッドを 1 箇所で修正するだけで済みます。
