# ローカル変数

関数内で割り当てられた変数は非公開です。

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

この例では、`filename`、`portfolio`、`line`、`fields`、および`s`はローカル変数です。これらの変数は関数呼び出しの後に保持されたり、アクセス可能ではありません。

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

ローカル変数は他の場所で見つかる変数とも競合しません。
