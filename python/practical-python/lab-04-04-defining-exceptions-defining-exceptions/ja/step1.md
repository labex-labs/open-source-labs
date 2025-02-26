# 演習4.11: カスタム例外の定義

ライブラリで独自の例外を定義することは、多くの場合、良い慣例です。

これにより、一般的なプログラミングエラーに応答して発生するPython例外と、特定の使用問題を示すためにライブラリによって意図的に発生させる例外とを区別しやすくなります。

前回の演習の `create_formatter()` 関数を変更して、ユーザーが不正なフォーマット名を提供した場合にカスタムの `FormatError` 例外を発生させるようにします。

たとえば：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
