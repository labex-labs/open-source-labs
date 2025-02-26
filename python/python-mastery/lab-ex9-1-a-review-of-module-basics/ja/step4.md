# from module import

Python を再起動して、モジュールから選択されたシンボルをインポートします。

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
>>>
```

これがモジュール全体を読み込んだ方法に注意してください（print 関数の出力と `x` 変数の使用方法を観察してください）。

`from` を使用すると、モジュールオブジェクト自体は見えなくなります。たとえば：

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name'simplemod' is not defined
>>>
```

モジュールから何かをエクスポートするとき、それらは単なる名前参照であることを理解しておくことが重要です。たとえば、これを試して説明してください：

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x is 42
>>> x = 13
>>> foo()
x is 42                   #!! 説明してください
>>> x
13
>>>
```
