# Importation des bibliothèques

Nous commencerons par importer les bibliothèques nécessaires. Nous utiliserons scikit-learn pour effectuer la classification par plus proches voisins et l'analyse NCA. Nous utiliserons matplotlib pour tracer les limites de décision de classe.

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
