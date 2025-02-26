# クラスメソッド

`@classmethod` は、クラスメソッドを定義するために使用されます。クラスメソッドは、インスタンスではなく、_クラス_ オブジェクトを最初のパラメータとして受け取るメソッドです。

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # インスタンス `f`
>>> Foo.spam()
<class '__main__.Foo'>              # クラス `Foo`
>>>
```

クラスメソッドは、主に代替コンストラクタを定義するためのツールとして使用されます。

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # クラスが引数として渡される方法に注意
        tm = time.localtime()
        # そして新しいインスタンスを作成するために使用される
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

クラスメソッドは、継承などの機能に関するいくつかの難しい問題を解決します。

```python
class Date:
  ...
    @classmethod
    def today(cls):
        # 正しいクラス（たとえば `NewDate`）を取得する
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
  ...

d = NewDate.today()
```
