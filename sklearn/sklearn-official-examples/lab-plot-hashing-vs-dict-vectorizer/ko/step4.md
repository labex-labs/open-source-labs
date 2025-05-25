# FeatureHasher

`FeatureHasher`를 평가합니다. 이 메서드는 특징 (예: 토큰) 에 해시 함수를 적용하여 미리 정의된 길이의 벡터를 생성한 다음, 해시 값을 직접 특징 인덱스로 사용하고 결과 벡터를 해당 인덱스에서 업데이트하는 방법입니다.

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
