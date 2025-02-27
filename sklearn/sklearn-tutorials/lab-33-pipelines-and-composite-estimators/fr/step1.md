# Pipeline - Chaînage d'estimateurs

La classe `Pipeline` dans scikit-learn est utilisée pour chaîner plusieurs estimateurs en un seul. Cela vous permet d'appeler `fit` et `predict` une seule fois sur vos données pour ajuster une séquence complète d'estimateurs. Cela permet également une sélection conjointe de paramètres et aide à éviter les fuites de données lors de la validation croisée.

Pour créer un pipeline, vous devez fournir une liste de paires `(clé, valeur)`, où la `clé` est une chaîne de caractères pour identifier chaque étape et la `valeur` est un objet estimateur. Voici un exemple de création d'un pipeline avec un transformateur PCA et un classifieur SVM :

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

Vous pouvez accéder aux étapes d'un pipeline en utilisant l'indexation ou par nom :

```python
pipe.steps[0]  # accéder par index
pipe[0]  # équivalent à ce qui précède
pipe['reduce_dim']  # accéder par nom
```

Vous pouvez également utiliser la fonction `make_pipeline` comme raccourci pour construire des pipelines :

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
