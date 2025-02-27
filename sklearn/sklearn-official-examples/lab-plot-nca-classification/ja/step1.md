# ライブラリのインポート

必要なライブラリをインポートして始めましょう。最近傍法による分類とNCAを実行するためにscikit-learnを使用します。クラス決定境界をプロットするためにmatplotlibを使用します。

```python
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import Pipeline
from sklearn.inspection import DecisionBoundaryDisplay
```
