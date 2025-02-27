# ライブラリのインポート

この実験に必要なライブラリをインポートして始めましょう。scikit-learnライブラリを使用してデータセットを生成し、ロジスティック回帰モデルを学習し、matplotlibライブラリを使用して決定境界を描画します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
