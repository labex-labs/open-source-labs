# すべてのエクスポート

`structly/__init__.py` で、すべてのエクスポートされるシンボルを含む `__all__` 変数を定義します。これを行った後、`stock.py` ファイルをさらに簡略化できるようになります。

```python
# stock.py

from structly import *

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
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

余談ですが、`from module import *` 文の使用は、一般的にPythonコミュニティでは非難されています。特に、何をしているか分からない場合にはそうです。とはいえ、ある状況ではそれが理にかなっていることもあります。たとえば、パッケージが多数の一般的に使用されるシンボルや定数を定義している場合、それを使用することが便利かもしれません。
