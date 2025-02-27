# Importar bibliotecas

Comenzaremos importando las bibliotecas necesarias. Utilizaremos scikit-learn para realizar la clasificación de vecinos más cercanos y el NCA. Utilizaremos matplotlib para graficar los límites de decisión de clase.

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
