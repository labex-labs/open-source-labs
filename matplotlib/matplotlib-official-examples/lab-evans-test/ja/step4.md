# カスタム単位クラスの登録

このステップでは、カスタム単位クラス - `Foo` をコンバータークラス - `FooConverter` に登録します。

```python
units.registry[Foo] = FooConverter()
```
