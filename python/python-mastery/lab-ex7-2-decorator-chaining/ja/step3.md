# 複数のデコレータとメソッド

デコレータをクラス内のメソッドに適用する場合、ややこしくなることがあります。次のクラスのメソッドに `@logged` デコレータを適用してみてください。

```python
class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass
```

これがまったく機能するでしょうか？（ヒント：いいえ）。コードを修正して機能させる方法はありますか？たとえば、次の例が機能するようにできますか？

```python
>>> s = Spam()
>>> s.instance_method()
instance_method
>>> Spam.class_method()
class_method
>>> Spam.static_method()
static_method
>>> s.property_method
property_method
>>>
```
