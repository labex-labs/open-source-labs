# モジュールの繰り返し読み込み

モジュールは一度だけ読み込まれることを理解しておくことが重要です。繰り返しインポートして、`print` 関数の出力が表示されないことに注意してください。

```python
>>> import simplemod
>>>
```

`x` の値を変更して、繰り返しインポートが影響を与えないことを確認してください。

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

モジュールを強制的に再読み込みしたい場合は、`importlib.reload()` を使用します。

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` は、すべての読み込まれたモジュールの辞書です。見てみて、モジュールを削除して、繰り返しインポートしてみてください。

```python
>>> sys.modules
... 出力を見る...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>>
```
