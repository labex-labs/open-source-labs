# エラーと例外

関数は例外としてエラーを報告します。例外は関数を中止させ、処理されない場合にはプログラム全体を停止させる可能性があります。

Python の REPL でこれを試してみてください。

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

デバッグ目的で、メッセージには何が起こったか、エラーが発生した場所、および失敗に至った他の関数呼び出しを示すトレースバックが記載されています。
