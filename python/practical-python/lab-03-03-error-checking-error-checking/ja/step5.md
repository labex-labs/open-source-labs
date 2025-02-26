# 例外値

例外には関連付けられた値があります。それは何が間違っているかに関するより具体的な情報を含んでいます。

```python
raise RuntimeError('Invalid user name')
```

この値は、`except` に渡される変数に格納される例外インスタンスの一部です。

```python
try:
 ...
except RuntimeError as e:   # `e` には発生した例外が格納されます
 ...
```

`e` は例外型のインスタンスです。ただし、印刷すると文字列のように見えることがよくあります。

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
