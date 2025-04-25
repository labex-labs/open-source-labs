# ライブラリのインポート

この実験に必要なライブラリをインポートして始めましょう。合成データセットを作成するために scikit-learn を、MLP モデルを構築するために MLPClassifier を、データを標準化するために StandardScaler を、変換と分類器のパイプラインを作成するために make_pipeline を使用します。

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```
