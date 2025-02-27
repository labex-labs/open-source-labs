# Bibliotheken importieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic, ExpSineSquared, ConstantKernel, DotProduct, Matern
```
