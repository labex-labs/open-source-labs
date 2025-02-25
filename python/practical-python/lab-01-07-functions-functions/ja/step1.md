# カスタム関数

再利用したいコードには関数を使用します。以下は関数の定義です。

```python
def sumcount(n):
    '''
    最初の n 個の整数の合計を返す
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

関数を呼び出すには、

```python
a = sumcount(100)
```

関数は、何らかのタスクを実行して結果を返す一連の文です。関数の戻り値を明示的に指定するには、`return` キーワードが必要です。
