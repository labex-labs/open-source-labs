# 抽象基底クラス

`TableFormatter` 基底クラスを変更して、`abc` モジュールを使用して適切な抽象基底クラスとして定義します。これを行ったら、この実験を試してみてください。

```python
>>> class NewFormatter(TableFormatter):
        def headers(self, headings):
            pass
        def row(self, rowdata):
            pass

>>> f = NewFormatter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class NewFormatter with abstract methods headings
>>>
```

ここでは、抽象基底クラスがクラス内のスペルミスをキャッチしました。つまり、`headings()` メソッドが誤って `headers()` とされていたという事実です。
