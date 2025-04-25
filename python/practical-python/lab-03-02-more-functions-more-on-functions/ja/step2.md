# デフォルト引数

時には、引数を省略可能にしたい場合があります。その場合は、関数定義でデフォルト値を割り当てます。

```python
def read_prices(filename, debug=False):
 ...
```

デフォルト値が割り当てられている場合、その引数は関数呼び出しで省略可能です。

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_注：デフォルト値のある引数は、引数リストの末尾に配置する必要があります (すべての必須引数は先頭に配置します)。_
