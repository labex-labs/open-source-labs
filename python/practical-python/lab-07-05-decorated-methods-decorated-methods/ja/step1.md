# 事前定義済みのデコレータ

クラス定義において特別な種類のメソッドを指定するために使用される事前定義済みのデコレータがあります。

```python
class Foo:
    def bar(self,a):
     ...

    @staticmethod
    def spam(a):
     ...

    @classmethod
    def grok(cls,a):
     ...

    @property
    def name(self):
     ...
```

順に見ていきましょう。
