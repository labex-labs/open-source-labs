# 演習1.13：個々の文字と部分文字列の抽出

文字列は文字の配列です。いくつかの文字を抽出してみましょう。

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # 最後の文字
?
>>> symbols[-2]        # 負のインデックスは文字列の末尾から始まります
?
>>>
```

Pythonでは、文字列は読み取り専用です。

`symbols` の最初の文字を小文字の 'a' に変更してみることでこれを確認しましょう。

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
