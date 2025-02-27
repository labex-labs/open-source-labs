# Bibliotheken importieren

Wir beginnen, indem wir die erforderlichen Bibliotheken für dieses Lab importieren. Wir verwenden die scikit-learn-Bibliothek, um den Datensatz zu generieren und die logistischen Regressionsmodelle zu trainieren, und die matplotlib-Bibliothek, um die Entscheidungsgrenze zu zeichnen.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
