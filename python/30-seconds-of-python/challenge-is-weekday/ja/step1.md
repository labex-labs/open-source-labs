# 日付が平日かどうかを確認する

## 問題

Pythonの関数`is_weekday()`を書きます。この関数は日付を入力として受け取り、平日の場合は`True`を返し、休日の場合は`False`を返します。日付が指定されていない場合は、関数は現在の日付を使用します。

この問題を解決するには、次の手順を辿ることができます。

1. `datetime`モジュールをインポートします。
2. `is_weekday()`という名前の関数を定義します。この関数は日付を入力として受け取ります。日付が指定されていない場合は、現在の日付を使用します。
3. `datetime`モジュールの`weekday()`メソッドを使用して、曜日を整数として取得します。`weekday()`メソッドは0（月曜日）から6（日曜日）の整数を返します。
4. 曜日が4以下であるかどうかを確認します。そうであれば`True`を返し、そうでなければ`False`を返します。

## 例

ここに、関数の動作の例をいくつか示します。

```python
from datetime import date

assert is_weekday(date(2022, 11, 11)) == False
assert is_weekday(date(2022, 11, 14)) == True
assert is_weekday(date(2022, 11, 12)) == False
assert is_weekday(date(2022, 11, 13)) == False
```
