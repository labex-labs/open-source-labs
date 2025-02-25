# 必要なライブラリとデータのインポート

まず、Pandas ライブラリとタイタニック号のデータセットをインポートする必要があります。

```python
# Import pandas library
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("data/titanic.csv")
titanic.head()
```
