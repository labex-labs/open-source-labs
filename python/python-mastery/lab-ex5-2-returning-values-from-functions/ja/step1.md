# 複数の値の返却

次のような行で構成される設定ファイルを解析するコードを書いているとしましょう。

    name=value

このような行を受け取り、関連付けられた名前と値の両方を返す関数 `parse_line(line)` を書きます。複数の値を返す際の一般的な慣例は、タプルで返すことです。たとえば：

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> name, val = parse_line('email=guido@python.org')
>>> name
'email'
>>> val
'guido@python.org'
>>>
```
