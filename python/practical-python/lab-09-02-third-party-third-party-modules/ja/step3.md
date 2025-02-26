# サードパーティモジュール

サードパーティモジュールは通常、専用の `site-packages` ディレクトリに配置されます。上記と同じ手順を行えばそれがわかります。

```python
>>> import numpy
>>> numpy
<module 'numpy' from '/usr/local/lib/python3.6/site-packages/numpy/__init__.py'>
>>>
```

再び、何かが `import` に関連して期待通りに機能しない原因を突き止めようとしている場合、モジュールを見ることは良いデバッグヒントになります。
