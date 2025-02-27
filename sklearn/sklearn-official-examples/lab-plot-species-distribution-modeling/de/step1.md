# Bibliotheken importieren

In diesem Schritt werden wir die erforderlichen Bibliotheken für unsere Analyse importieren. Wir werden die scikit-learn-Bibliothek für maschinelles Lernen, numpy für numerische Berechnungen und matplotlib für die Visualisierung importieren.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
