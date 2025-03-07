# 例外のキャッチと処理

例外をキャッチして処理することができます。

キャッチするには、`try - except` 文を使用します。

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
  ...
```

`ValueError` という名前は、キャッチしようとしているエラーの種類と一致する必要があります。

実行中の操作に応じて、事前にどのような種類のエラーが発生するかを正確に把握することはしばしば困難です。良くも悪くも、例外処理はしばしばプログラムが予期せずクラッシュした後に追加されます（つまり、「ああ、そのエラーをキャッチするのを忘れていました。それを処理する必要があります！」）。
