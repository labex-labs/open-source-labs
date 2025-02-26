# 演習2.18：カウンターを使った集計

各銘柄の株式の総数を集計したいとしましょう。`Counter` オブジェクトを使うとこれは簡単です。試してみましょう：

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

`portfolio` にある `MSFT` と `IBM` の複数のエントリがここで単一のエントリにどのように結合されるかを注意深く観察してください。

個々の値を取得するためには、辞書と同じように `Counter` を使うことができます：

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

値をランキング付けしたい場合は、次のようにします：

```python
>>> # 保有株数が最も多い銘柄トップ3を取得
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

別の株式のポートフォリオを取得して新しい `Counter` を作成しましょう：

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

最後に、すべての保有株を1つの簡単な操作で結合しましょう：

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

これは `Counter` が提供する機能の一部にすぎません。ただし、値を集計する必要がある場合、`Counter` を使うことを検討する必要があります。
