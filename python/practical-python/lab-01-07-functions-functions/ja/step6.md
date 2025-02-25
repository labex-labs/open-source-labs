# 演習1.29：関数の定義

簡単な関数を定義してみましょう：

```python
>>> def greeting(name):
        'Issues a greeting'
        print('Hello', name)

>>> greeting('Guido')
Hello Guido
>>> greeting('Paula')
Hello Paula
>>>
```

関数の最初の文が文字列の場合、それはドキュメントとして機能します。`help(greeting)` のようなコマンドを入力して、表示されるかどうかを確認してみてください。
