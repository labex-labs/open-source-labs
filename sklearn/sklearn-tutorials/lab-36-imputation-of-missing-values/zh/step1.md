# 导入必要的模块

首先，我们需要从scikit-learn库中导入所需的模块。我们将使用`SimpleImputer`类进行单变量特征插补，使用`IterativeImputer`类进行多变量特征插补。

```python
import numpy as np
from sklearn.impute import SimpleImputer, IterativeImputer
```
