# 必要なモジュールをインポートする

まず、scikit-learnライブラリから必要なモジュールをインポートする必要があります。単変量特徴量の欠損値補完には`SimpleImputer`クラスを、多変量特徴量の欠損値補完には`IterativeImputer`クラスを使用します。

```python
import numpy as np
from sklearn.impute import SimpleImputer, IterativeImputer
```
