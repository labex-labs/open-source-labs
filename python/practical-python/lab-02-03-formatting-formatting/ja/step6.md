# 演習2.8：数値の書式設定方法

数値を表示する際の一般的な問題は、小数桁数を指定することです。これを解決する方法の1つは、f-文字列の使用です。これらの例を試してみてください。

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

f-文字列で使用される書式設定コードの完全なドキュメントは、[ここ](https://docs.python.org/3/library/string.html#format-specification-mini-language)で見つけることができます。書式設定は、時々文字列の`%`演算子を使用しても行われます。

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

`%`と共に使用されるさまざまなコードのドキュメントは、[ここ](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)で見つけることができます。

`print`と共に一般的に使用されますが、文字列の書式設定は印刷に縛られるものではありません。フォーマット済みの文字列を保存したい場合は、変数に割り当てるだけです。

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
