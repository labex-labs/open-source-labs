# ライブラリのインポート

投票回帰器を使って糖尿病の予測を行うために必要なライブラリをインポートしましょう。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
```
