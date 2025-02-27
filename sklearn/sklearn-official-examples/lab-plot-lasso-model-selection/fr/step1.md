# Dataset

Tout d'abord, nous allons charger le jeu de données sur le diabète à l'aide de la fonction `load_diabetes` de `sklearn.datasets`. Le jeu de données est composé de 10 variables de base, l'âge, le sexe, l'indice de masse corporelle, la pression artérielle moyenne et six mesures de sérum sanguin, et une mesure quantitative de la progression de la maladie un an après le stade initial.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
