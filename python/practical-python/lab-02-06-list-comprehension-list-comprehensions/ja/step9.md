# 演習 2.22: データ抽出

`name`と`shares`が`portfolio`から取得される、タプル`(name, shares)`のリストをどのように作成できるかを示しましょう。

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

四角かっこ（`[`, `]`）を波かっこ（`{`, `}`）に変えると、セット内包表記と呼ばれるものが得られます。これにより、一意または異なる値が得られます。

たとえば、`portfolio`に現れる一意の株式名のセットを決定します。

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

`key:value`ペアを指定すると、辞書を作成できます。たとえば、株式の名前を保有株式の総数にマッピングする辞書を作成します。

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

後者の機能は**辞書内包表記**と呼ばれます。表にまとめましょう。

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

`prices`辞書を、ポートフォリオに現れる名前のみに絞り込むこの例を試してみましょう。

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
