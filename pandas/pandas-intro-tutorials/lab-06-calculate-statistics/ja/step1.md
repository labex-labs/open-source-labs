# データセットのインポート

最初のステップは、使用するデータセットをインポートすることです。

```python
# pandas ライブラリのインポート
import pandas as pd

# データセットの読み込み
titanic = pd.read_csv("data/titanic.csv")

# データセットの最初の 5 行を表示
titanic.head()
```
