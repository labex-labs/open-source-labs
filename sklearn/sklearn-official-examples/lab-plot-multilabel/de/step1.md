# Bibliotheken importieren

In diesem Schritt importieren wir die erforderlichen Bibliotheken: `numpy`, `matplotlib`, `make_multilabel_classification` aus `sklearn.datasets`, `OneVsRestClassifier` und `SVC` aus `sklearn.multiclass`, `PCA` und `CCA` aus `sklearn.decomposition`.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
