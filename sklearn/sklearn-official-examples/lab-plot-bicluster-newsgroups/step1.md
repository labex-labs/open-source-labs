# Import Libraries

We will import the necessary libraries for this lab.

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


