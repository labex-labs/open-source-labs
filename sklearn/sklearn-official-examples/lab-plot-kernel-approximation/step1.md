# Python Package and Dataset Imports, Load Dataset

```python
# Standard scientific Python imports
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# The digits dataset
digits = datasets.load_digits(n_class=9)
```
