# Importieren der erforderlichen Bibliotheken

Zunächst müssen wir die erforderlichen Bibliotheken importieren.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import DotProduct, ConstantKernel as C
```
