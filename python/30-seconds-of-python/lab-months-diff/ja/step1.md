# Python における日付オブジェクトの理解

日付間の月数の差を計算する前に、Python で日付オブジェクトを扱う方法を理解する必要があります。このステップでは、`datetime` モジュールについて学び、いくつかの日付オブジェクトを作成します。

まず、プロジェクトディレクトリに新しい Python ファイルを作成しましょう。WebIDE を開き、左側のエクスプローラーパネルにある「新しいファイル」アイコンをクリックします。ファイル名を `month_difference.py` とし、`/home/labex/project` ディレクトリに保存します。

必要なモジュールをインポートするために、以下のコードを追加します。

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

ファイルを保存し、ターミナルを使用して実行します。

```bash
python3 ~/project/month_difference.py
```

以下のような出力が表示されるはずです。

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

`datetime` モジュールの `date` クラスを使用すると、年、月、日を指定して日付オブジェクトを作成できます。ある日付から別の日付を引くと、Python は `timedelta` オブジェクトを返します。このオブジェクトの日数には、`.days` 属性を使用してアクセスできます。

この例では、2023 年 1 月 15 日と 2023 年 3 月 20 日の間には 64 日あります。
