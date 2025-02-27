# Bibliotheken importieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken. Wir werden scikit-learn verwenden, um die Klassifizierung mit nächsten Nachbarn und NCA durchzuführen. Wir werden matplotlib verwenden, um die Klassifizierungsgrenzen zu plotten.

```python
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import Pipeline
from sklearn.inspection import DecisionBoundaryDisplay
```
