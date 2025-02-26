# メソッド解決順序 (Method Resolution Order: MRO)

Python は継承チェーンを事前に計算し、それをクラスの `_MRO_` 属性に格納します。これを確認することができます。

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

このチェーンは **メソッド解決順序** と呼ばれます。属性を見つけるために、Python はこの MRO を順に辿ります。最初の一致が採用されます。
