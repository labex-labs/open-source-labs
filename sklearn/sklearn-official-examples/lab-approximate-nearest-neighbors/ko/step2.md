# 필요한 라이브러리 가져오기

필요한 라이브러리, `nmslib`, `pynndescent`, `sklearn`, `numpy`, `scipy`, `matplotlib` 등을 가져와야 합니다.

```python
import sys
import joblib
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.datasets import fetch_openml
from sklearn.utils import shuffle
from sklearn.manifold import TSNE
from sklearn.neighbors import KNeighborsTransformer
from sklearn.pipeline import make_pipeline
from pynndescent import PyNNDescentTransformer
import nmslib
```
