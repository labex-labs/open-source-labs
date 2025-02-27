# Bibliotheken importieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken für dieses Lab. Wir werden scikit-learn verwenden, um synthetische Datensätze zu erstellen, MLPClassifier, um das MLP-Modell zu erstellen, StandardScaler, um die Daten zu standardisieren, und make_pipeline, um eine Pipeline von Transformationen und Klassifizierern zu erstellen.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```
