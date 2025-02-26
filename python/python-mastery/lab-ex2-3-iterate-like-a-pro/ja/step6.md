# ジェネレータ式と集約関数

ジェネレータ式は、`sum()`、`min()`、`max()`、`any()` などの関数にデータを供給する際に特に便利です。以前のポートフォリオデータを使っていくつかの例を試してみましょう。これらの例では、リスト内包表記を使用したときに現れた余分な角括弧（\[\]）が欠けていることに注意してください。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

コンマ区切りの値を作成する際のジェネレータ式の巧妙な使い方を以下に示します：

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... 失敗することに注意...
>>> ','.join(str(x) for x in s)    # これは機能します
'GOOG,100,490.1'
>>>
```

上記の例の構文は少し慣れる必要がありますが、重要なポイントは、どの操作も結果の完全に埋め尽くされたリストを作成しないことです。これにより、メモリを大幅に節約できます。ただし、構文を過度に使いすぎないように注意する必要があります。
