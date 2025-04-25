# 月数の差を計算する関数の作成

日付オブジェクトの扱いと日数の差の計算方法がわかったので、月数の差を計算する関数を作成しましょう。

多くのアプリケーションでは、1 か月を 30 日と近似します。これは必ずしも正確ではありません（月には 28 日から 31 日まであります）が、多くのビジネス計算では有効な一般的な簡略化です。

`month_difference.py` ファイルを開き、既存のコードの下に以下の関数を追加します。

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

この関数が行うことを理解しましょう。

1. 2 つのパラメータ `start` と `end` を受け取ります。これらは日付オブジェクトです。
2. これらの日付間の日数の差を計算します。
3. 30 で割って日数を月数に変換します。
4. `ceil()` を使用して最も近い整数に切り上げます。
5. 結果を整数として返します。

`ceil()` 関数を使用するのは、多くのビジネスシナリオでは、請求目的で部分的な月でも 1 か月としてカウントされるためです。

関数をテストするために、ファイルの末尾に以下のコードを追加します。

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

ファイルを保存し、再度実行します。

```bash
python3 ~/project/month_difference.py
```

以下のような出力が表示されるはずです。

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

以下の点に注意してください。

- 2023 年 1 月 15 日と 2023 年 3 月 20 日の間の 64 日は、3 か月として計算されます（64/30 = 2.13 を切り上げて 3）。
- 10 月 28 日と 11 月 25 日の差は、1 か月として計算されます。
- 12 月 15 日と 1 月 10 日の差（年をまたぐ）も、1 か月として計算されます。
