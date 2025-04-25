# 演習 1.16：文字列のメソッド

Python の対話型プロンプトで、いくつかの文字列のメソッドを試してみましょう。

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

文字列は常に読み取り専用であることを忘れないでください。操作の結果を保存したい場合は、それを変数に格納する必要があります。

```python
>>> lowersyms = symbols.lower()
>>>
```

さらにいくつかの操作を試してみましょう。

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name = '   IBM   \n'
>>> name = name.strip()    # 周囲の空白を削除する
>>> name
?
>>>
```
