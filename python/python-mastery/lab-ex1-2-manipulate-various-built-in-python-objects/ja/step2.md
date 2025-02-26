# 第2部 : 文字列操作

次のように、株価の銘柄記号のシリーズを含む文字列を定義します。

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

では、さまざまな文字列操作を試してみましょう。

## 個々の文字と部分文字列の抽出

文字列は文字の配列です。いくつかの文字を抽出してみましょう。

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # 最後の文字
'O'
>>> symbols[-2]        # 最後から2番目の文字
'C'
>>>
```

いくつかのスライスを試してみましょう。

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## 読み取り専用オブジェクトとしての文字列

文字列は読み取り専用です。`symbols` の最初の文字を小文字の 'a' に変更しようとして、これを確認してみましょう。

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

## 文字列の連結

文字列データは読み取り専用ですが、常に新しく作成された文字列を変数に再割り当てることができます。\
次のステートメントを試してみてください。これは新しいシンボル "GOOG" を `symbols` の末尾に連結します。

```python
>>> symbols += ' GOOG'
>>> symbols
... 結果を見てください...
```

次に、このようにして `symbols` の先頭に "HPQ" を追加してみましょう。

```python
>>> symbols = 'HPQ'+ symbols
>>> symbols
... 結果を見てください...
```

これらの例の両方では、元の文字列 `symbols` が「その場で」変更されているわけではありません。代わりに、完全に新しい文字列が作成されます。変数名 `symbols` は単に結果にバインドされています。その後、古い文字列はもはや使用されないので破棄されます。

## メンバーシップテスト（部分文字列テスト）

`in` 演算子を使って部分文字列をチェックしてみましょう。対話型プロンプトで、次の操作を試してください。

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

「AA」のチェックが `True` を返した理由を理解してください。

## 文字列メソッド

Python の対話型プロンプトで、いくつかの文字列メソッドを試してみましょう。

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

忘れないでください。文字列は常に読み取り専用です。操作の結果を保存したい場合は、変数に格納する必要があります。

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

さらにいくつかの操作を試してみましょう。

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```
