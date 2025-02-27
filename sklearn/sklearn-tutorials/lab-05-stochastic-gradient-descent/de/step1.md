# Importieren der erforderlichen Bibliotheken

Zunächst müssen wir die erforderlichen Bibliotheken importieren. Wir werden die scikit-learn-Bibliothek für die maschinelle Lernung und die Datenaufbereitung verwenden.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
