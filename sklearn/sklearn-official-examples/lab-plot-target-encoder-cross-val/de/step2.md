# Importieren der erforderlichen Bibliotheken

Als nächstes müssen wir die erforderlichen Bibliotheken importieren. Führen Sie den folgenden Code aus, um die erforderlichen Bibliotheken zu importieren:

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer, TargetEncoder
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
```