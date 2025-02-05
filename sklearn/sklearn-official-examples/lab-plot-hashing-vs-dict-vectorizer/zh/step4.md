# 特征哈希器

我们将对“特征哈希器（FeatureHasher）”进行基准测试，它是一种通过对特征（例如词元）应用哈希函数来构建预定义长度向量的方法，然后直接将哈希值用作特征索引，并在这些索引处更新结果向量。

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

t0 = time()
hasher = FeatureHasher(n_features=2**18)
X = hasher.transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")
print(f"Found {len(np.unique(X.nonzero()[1]))} unique tokens")
```
