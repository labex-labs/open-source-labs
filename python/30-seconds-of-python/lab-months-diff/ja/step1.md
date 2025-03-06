# Pythonにおける日付オブジェクトの理解

日付間の月数の差を計算する前に、Pythonで日付オブジェクトを扱う方法を理解する必要があります。このステップでは、`datetime` モジュールについて学び、いくつかの日付オブジェクトを作成します。

まず、プロジェクトディレクトリに新しいPythonファイルを作成しましょう。WebIDEを開き、左側のエクスプローラーパネルにある「新しいファイル」アイコンをクリックします。ファイル名を `month_difference.py` とし、`/home/labex/project` ディレクトリに保存します。

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

`datetime` モジュールの `date` クラスを使用すると、年、月、日を指定して日付オブジェクトを作成できます。ある日付から別の日付を引くと、Pythonは `timedelta` オブジェクトを返します。このオブジェクトの日数には、`.days` 属性を使用してアクセスできます。

この例では、2023年1月15日と2023年3月20日の間には64日あります。
