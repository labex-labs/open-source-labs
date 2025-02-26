# 関数の呼び出し

この関数を考えてみましょう。

```python
def read_prices(filename, debug):
  ...
```

位置引数を使って関数を呼び出すことができます。

    prices = read_prices('prices.csv', True)

または、キーワード引数を使って関数を呼び出すこともできます。

```python
prices = read_prices(filename='prices.csv', debug=True)
```
