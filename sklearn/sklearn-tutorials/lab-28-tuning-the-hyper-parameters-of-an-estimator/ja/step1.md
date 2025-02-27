# 必要なライブラリをインポートする

まず、分析に必要なライブラリをインポートする必要があります。ハイパーパラメータの調整を行うために、`sklearn.model_selection` を使用します。

```python
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
```
