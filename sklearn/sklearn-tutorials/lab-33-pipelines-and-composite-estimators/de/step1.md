# Pipeline - Kette von Schätzern

Die `Pipeline`-Klasse in scikit-learn wird verwendet, um mehrere Schätzer zu einer einzigen Kette zu verketten. Dies ermöglicht es Ihnen, einmal `fit` und `predict` auf Ihren Daten aufzurufen, um eine ganze Sequenz von Schätzern anzupassen. Es ermöglicht auch die gemeinsame Parameterauswahl und hilft dabei, Datenleckage bei der Kreuzvalidierung zu vermeiden.

Um eine Pipeline zu erstellen, müssen Sie eine Liste von `(Schlüssel, Wert)`-Paaren angeben, wobei der `Schlüssel` ein String ist, um jeden Schritt zu identifizieren, und der `Wert` ein Schätzerobjekt ist. Im Folgenden ist ein Beispiel für das Erstellen einer Pipeline mit einem PCA-Transformator und einem SVM-Klassifizierer:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

Sie können die Schritte einer Pipeline über Indexierung oder nach Namen zugreifen:

```python
pipe.steps[0]  # Zugang über Index
pipe[0]  # Äquivalent zu oben
pipe['reduce_dim']  # Zugang nach Namen
```

Sie können auch die `make_pipeline`-Funktion als Abkürzung für das Erstellen von Pipelines verwenden:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
