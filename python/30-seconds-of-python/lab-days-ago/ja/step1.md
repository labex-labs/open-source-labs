# 何日か前

あなたの課題は、整数 `n` を引数として受け取り、今日から `n` 日前の日付を返す `days_ago(n)` という関数を書くことです。

この問題を解決するには、`datetime` モジュールの `date` クラスを使って現在の日付を取得し、`timedelta` クラスを使って現在の日付から `n` 日を引きます。

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
