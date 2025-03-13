# stock.py プログラムの更新とテスト

パッケージを作成し、内部のインポートを修正したので、次は `stock.py` ファイルを更新して新しいパッケージ構造を使用するようにしましょう。Python のパッケージは、関連するモジュールをまとめる方法です。これにより、コードベースを整理し、コードの管理と再利用が容易になります。

エディタで `stock.py` ファイルを開きます。

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

現在の `stock.py` のインポート文は、すべてのファイルが同じディレクトリにある古い構造を前提としています。Python でモジュールをインポートすると、Python は特定の場所でモジュールを探します。古い構造では、すべてのファイルが同じディレクトリにあったため、Python はモジュールを簡単に見つけることができました。しかし、新しいパッケージ構造では、`structly` パッケージ内のモジュールを Python に探す場所を教えるために、インポート文を更新する必要があります。

`stock.py` ファイルを以下のように更新します。

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

主な変更点は以下の通りです。

1. `from structure import Structure, String, PositiveInteger, PositiveFloat` を `from structly.structure import Structure, String, PositiveInteger, PositiveFloat` に変更しました。この変更により、Python は `structly` パッケージ内の `structure` モジュールを探すようになります。
2. `from reader import read_csv_as_instances` を `from structly.reader import read_csv_as_instances` に変更しました。同様に、この変更により、Python は `structly` パッケージ内の `reader` モジュールを探すようになります。
3. `from tableformat import create_formatter, print_table` を `from structly.tableformat import create_formatter, print_table` に変更しました。これにより、Python は `structly` パッケージ内の `tableformat` モジュールを見つけることができます。

これらの変更を加えたら、ファイルを保存します。ファイルを保存することは、変更を保存し、プログラムを実行するときに使用できるようにするために重要です。

では、更新したコードをテストして、すべてが正しく動作することを確認しましょう。

```bash
python stock.py
```

以下の出力が表示されるはずです。

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

この出力が表示されたら、おめでとうございます！Python パッケージを正常に作成し、コードを更新して使用することができました。これは、コードがよりモジュール化された方法で整理され、将来的なメンテナンスと拡張が容易になったことを意味します。
