# モジュールの読み込みとシステムパス

先ほど作成したモジュールをインポートしてみましょう。

```python
>>> import simplemod
Loaded simplemod
>>> simplemod.foo()
x is 42
>>>
```

これが `ImportError` で失敗した場合、パス設定が不安定です。`sys.path` の値を見て修正してください。

```python
>>> import sys
>>> sys.path
... 結果を見る...
>>>
```
