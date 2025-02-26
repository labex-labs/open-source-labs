# Lambda：匿名関数

関数を作成する代わりにlambdaを使用します。先ほどのソートの例では、

```python
portfolio.sort(key=lambda s: s['name'])
```

これは、_単一の_ 式を評価する _名前のない_ 関数を作成します。上記のコードは、最初のコードよりもはるかに短くなっています。

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
