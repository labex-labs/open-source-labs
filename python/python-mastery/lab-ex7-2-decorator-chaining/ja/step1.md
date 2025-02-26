# メタデータのコピー

関数がデコレータによってラップされるとき、関数の名前、ドキュメント文字列、その他の詳細に関する情報が失われることがよくあります。これを確認しましょう。

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... 出力を見てください...
>>>
```

`logged` デコレータの定義を修正して、関数のメタデータを適切にコピーするようにします。これを行うには、ノートに示すように `@wraps(func)` デコレータを使用します。

完了した後、デコレータが関数名とドキュメント文字列を保持することを確認します。

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

以前に書いた `@validated` デコレータも、`@wraps(func)` を使用してメタデータを保持するように修正します。
