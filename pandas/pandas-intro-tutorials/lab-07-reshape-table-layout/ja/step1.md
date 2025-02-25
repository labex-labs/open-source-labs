# ライブラリのインポートとデータの読み込み

まず、必要なライブラリをインポートしてデータセットを読み込みましょう。

```python
import pandas as pd

# チタニック号のデータセットを読み込む
titanic = pd.read_csv("data/titanic.csv")

# 大気質のデータセットを読み込む
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
