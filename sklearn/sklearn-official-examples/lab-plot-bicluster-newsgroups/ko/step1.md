# 라이브러리 가져오기

이 실습에 필요한 라이브러리를 가져옵니다.

```python
from collections import defaultdict
import operator
from time import time
import numpy as np
from sklearn.cluster import SpectralCoclustering
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.cluster import v_measure_score
```
