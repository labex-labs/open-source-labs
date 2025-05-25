# Importar Bibliotecas

Começaremos importando as bibliotecas necessárias. Usaremos o scikit-learn para realizar a classificação de vizinhos mais próximos e a NCA. Usaremos o matplotlib para plotar os limites de decisão de classe.

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
