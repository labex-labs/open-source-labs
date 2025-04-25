# 「ミックスイン」パターン

「ミックスイン」パターンは、コードの断片を持つクラスです。

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

このクラスは単独では使用できません。継承を通じて他のクラスと混合します。

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

不思議なことに、大音量の機能が今度は一度だけ実装され、2 つのまったく関係のないクラスで再利用されました。このようなトリックは、Python における多重継承の主な用途の 1 つです。
