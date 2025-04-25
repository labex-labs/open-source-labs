# モジュールとインポート

任意の Python ソースファイルはモジュールです。

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

`import`文はモジュールを読み込み、*実行*します。

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
