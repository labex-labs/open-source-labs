# 必要なライブラリをインポートしてデータを読み込む

まず、必要なPythonライブラリをインポートして、大気質データを読み込む必要があります。このデータは、2次元のラベル付きデータ構造であるpandasのDataFrameに読み込まれます。

```python
# 必要なライブラリをインポートする
import pandas as pd
import matplotlib.pyplot as plt

# 大気質データを読み込む
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# "date.utc" 列を "datetime" にリネームする
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
