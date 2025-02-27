# ライブラリのインポート

まず、必要なライブラリをインポートする必要があります。可視化には `matplotlib` を、データセットを読み込み評価するために `sklearn` の `datasets` と `metrics` を、サポートベクターマシンを学習するために `svm` を使用します。

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
