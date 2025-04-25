# 演習 1.14：文字列の連結

文字列データは読み取り専用ですが、常に新しく作成された文字列を変数に再代入することができます。

次の文を試してみてください。これは、新しいシンボル "GOOG" を `symbols` の末尾に連結します。

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

あっ！これは望んだ結果ではありません。修正して、`symbols` 変数に `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'` の値が入るようにしてください。

```python
>>> symbols =?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

文字列の先頭に `'HPQ'` を追加します。

```python
>>> symbols =?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

これらの例では、元の文字列が修正されているように見えるかもしれませんが、文字列が読み取り専用であることに反しているように見えます。そうではありません。文字列の操作は、毎回まったく新しい文字列を作成します。変数名 `symbols` が再代入されると、新しく作成された文字列にポイントが移ります。その後、古い文字列はもはや使用されないので破棄されます。
