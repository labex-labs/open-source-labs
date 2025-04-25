# モジュール

どの Python ソースファイルもモジュールです。

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

`import` 文はモジュールを読み込み、そして _実行_ します。

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
