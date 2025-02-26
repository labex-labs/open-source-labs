# モジュールの検索

Pythonは、モジュールを探す際にパスリスト（sys.path）を参照します。

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

通常、現在の作業ディレクトリが最初になります。
