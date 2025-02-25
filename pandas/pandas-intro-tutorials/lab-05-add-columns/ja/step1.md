# Pandas をインポートしてデータを読み込む

まず、pandas ライブラリをインポートし、CSV ファイルから空気質データを読み込みます。

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
