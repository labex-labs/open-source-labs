# 解説

インタプリタを使って実験を始めるとき、異なるオブジェクトがサポートする操作についてもっと知りたいことがよくあります。たとえば、文字列で利用可能な操作をどのように調べるかということです。

あなたのPython環境によっては、タブ補完を通じて利用可能なメソッドの一覧を見ることができるかもしれません。たとえば、次のように入力してみてください。

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

タブキーを押しても何も起こらない場合は、組み込みの `dir()` 関数に頼ることができます。たとえば：

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` は `(.)` の後に現れるすべての操作のリストを生成します。特定の操作に関する詳細情報を取得するには `help()` コマンドを使います。

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```
