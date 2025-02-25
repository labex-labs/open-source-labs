# 文字列の不変性

文字列は「不変」または読み取り専用です。作成されると、値を変更することはできません。

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**文字列データを操作するすべての操作とメソッドは、常に新しい文字列を作成します。**
