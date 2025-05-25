# 라이브러리 가져오기

이 단계에서는 필요한 라이브러리를 가져옵니다: `numpy`, `matplotlib`, `make_multilabel_classification` 함수는 `sklearn.datasets`에서 가져오고, `OneVsRestClassifier`와 `SVC`는 `sklearn.multiclass`에서, `PCA`와 `CCA`는 `sklearn.decomposition`에서 가져옵니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
