# 必要なライブラリをインポートしてデータを読み込む

まず、必要な Python ライブラリをインポートして、大気質データを読み込む必要があります。このデータは、2 次元のラベル付きデータ構造である pandas の DataFrame に読み込まれます。

```python
# 必要なライブラリをインポートする
import pandas as pd
import matplotlib.pyplot as plt

# 大気質データを読み込む
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# "date.utc" 列を "datetime" にリネームする
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
