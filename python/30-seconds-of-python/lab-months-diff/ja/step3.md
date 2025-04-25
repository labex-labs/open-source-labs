# 様々な日付シナリオでのテスト

`months_diff` 関数がさまざまな日付シナリオでどのように動作するかをよりよく理解するために、別のテストファイルを作成しましょう。このアプローチは、コードが期待通りに動作することを検証するためにソフトウェア開発で一般的に行われます。

`/home/labex/project` ディレクトリに `month_diff_test.py` という名前の新しいファイルを作成します。

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

このファイルを保存して実行します。

```bash
python3 ~/project/month_diff_test.py
```

以下のような出力が表示されるはずです。

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

これらの結果を分析してみましょう。

1. **同じ月**: 同じ月内の日付でも、関数は 1 か月を返します。これは、部分的な月でも 1 か月としてカウントされるためです。

2. **連続する月**: 連続する月の日付の場合、関数は 1 か月を返します。

3. **年をまたぐ**: 年をまたぐ日付の場合でも、関数は正しく計算します。

4. **数か月離れた日付**: 数か月離れた日付の場合、関数は適切な月数を計算します。

5. **逆順の日付**: 終了日が開始日より前の場合、負の結果が得られます。これは、残り時間の計算などのシナリオでは合理的です。

6. **30 日の倍数**: 正確に 30 日の場合、1 か月が得られます。60 日の場合、2 か月が得られます。これは、関数が月の定義の正確な倍数で期待通りに動作することを確認しています。

私たちの `months_diff` 関数は、月を 30 日と定義した場合、これらすべてのテストケースを正しく処理します。
