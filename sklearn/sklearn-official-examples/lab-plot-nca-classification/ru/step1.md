# Импорт библиотек

Начнем с импорта необходимых библиотек. Для выполнения классификации ближайших соседей и NCA будем использовать scikit-learn. Для построения границ решения классов будем использовать matplotlib.

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
