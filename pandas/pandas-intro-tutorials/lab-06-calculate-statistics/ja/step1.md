# データセットのインポート

最初のステップは、使用するデータセットをインポートすることです。

```python
# pandasライブラリのインポート
import pandas as pd

# データセットの読み込み
titanic = pd.read_csv("data/titanic.csv")

# データセットの最初の5行を表示
titanic.head()
```
