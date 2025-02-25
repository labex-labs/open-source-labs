# Bibliotheken importieren und Plot einrichten

Der erste Schritt besteht darin, die erforderlichen Bibliotheken zu importieren und den Plot einzurichten. In diesem Beispiel verwenden wir das `pyplot`-Modul von Matplotlib und dessen `3d`-Toolkit, um den 3D-Plot zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
