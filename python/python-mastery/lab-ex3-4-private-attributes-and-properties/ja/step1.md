# プライベート属性の実装

Python でクラスを設計する際には、クラス内部でのみ使用される特定の属性があります。これらの属性はクラスの内部実装の一部です。他の開発者にこれを示すために、命名規則に従います。これらの内部属性にはアンダースコア (`_`) を接頭辞として付けます。これは、これらの属性がパブリック API の一部ではないことを示す目印のようなものです。パブリック API は、コードの他の部分が相互作用することを想定されたメソッドと属性のセットです。したがって、アンダースコアが付いた属性はクラスの外部から直接アクセスすべきではありません。

`stock.py` ファイルの現在の `Stock` クラスを見てみましょう。このクラスは株式を表すために使用され、`types` という名前のクラス変数を持っています。

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

`types` クラス変数は、クラス内部で行データを変換するために使用されます。たとえば、行のデータを取得したときに、これらの型を使用してデータを正しい形式に変換します。これは単なる実装の詳細であり、コードの他の部分が直接相互作用すべきものではないため、これをプライベートとしてマークする必要があります。

## 手順：

1. まず、エディタで `stock.py` ファイルを開く必要があります。これは、ターミナルで次のコマンドを使用して行うことができます。このコマンドは、コードエディタでファイルを開きます。

   ```bash
   code /home/labex/project/stock.py
   ```

2. 次に、`types` クラス変数を変更します。先頭にアンダースコアを追加して `_types` にします。この変更は、この変数がプライベートであり、クラスの外部から直接アクセスすべきではないことを示します。

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. 変数を改名した後、`from_row` メソッドを更新する必要があります。このメソッドは、行データを変換するために `types` 変数を使用します。これを `_types` に改名したので、メソッドもそれに応じて更新する必要があります。

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. これらの変更を加えたら、ファイルを保存する必要があります。ファイルを保存することで、変更が保存され、後で使用できるようになります。

5. 変更をテストするために、`test_stock.py` という名前の Python スクリプトを作成します。次のコマンドを使用してエディタでファイルを開くことができます。

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. 次に、`test_stock.py` ファイルに次のコードを追加します。このコードは、`Stock` クラスのインスタンスを直接作成するとともに、`from_row` メソッドを使用して作成します。そして、これらのインスタンスに関する情報、たとえば名前、株式数、価格、およびコストを出力します。

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
   print(f"Cost: {s.cost()}")

   # Create from row
   row = ['AAPL', '50', '142.5']
   apple = Stock.from_row(row)
   print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
   print(f"Cost: {apple.cost()}")
   ```

7. 最後に、ターミナルで次のコマンドを使用してテストスクリプトを実行します。これにより、`test_stock.py` ファイルのコードが実行され、出力が表示されます。

   ```bash
   python /home/labex/project/test_stock.py
   ```

次のような出力が表示されるはずです。

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Name: AAPL, Shares: 50, Price: 142.5
Cost: 7125.0
```
