# Testdaten erstellen

Zunächst werden wir einige Testdaten erstellen, die wir für das Violindiagramm verwenden. Wir werden NumPy verwenden, um vier Arrays mit 100 normalverteilten Werten mit zunehmender Standardabweichung zu generieren.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
