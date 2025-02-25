# 今日からの日数

## 問題

整数 `n` を入力として受け取り、今日から `n` 日後の日付を返す関数 `days_from_now(n)` を書きなさい。

この問題を解くには、次の手順に従うことができます。

1. `datetime` モジュールをインポートする。
2. `date.today()` メソッドを使って現在の日付を取得する。
3. `timedelta` メソッドを使って現在の日付に `n` 日を加える。
4. 新しい日付を返す。

## 例

```python
>>> days_from_now(5)
datetime.date(2022, 12, 28)
>>> days_from_now(10)
datetime.date(2022, 1, 2)
```
