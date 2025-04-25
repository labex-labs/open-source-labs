# 演習 6.4：単純なジェネレータ

反復処理をカスタマイズしたいときは、常にジェネレータ関数を考えるべきです。書きやすいです。望ましい反復処理ロジックを実行する関数を作成し、値を発行するために `yield` を使用します。

たとえば、このジェネレータを試してみてください。これは、一致するサブ文字列を含む行をファイルから検索します。

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

これは面白いです。関数にカスタム処理を隠し、for ループに供給するために使用できるという考え方です。次の例は、もっと珍しいケースを見ています。
