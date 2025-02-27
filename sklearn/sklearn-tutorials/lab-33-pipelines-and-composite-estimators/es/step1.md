# Pipeline - Encadenamiento de Estimadores

La clase `Pipeline` en scikit-learn se utiliza para encadenar múltiples estimadores en uno solo. Esto le permite llamar a `fit` y `predict` una sola vez en sus datos para ajustar una secuencia completa de estimadores. También permite la selección conjunta de parámetros y ayuda a evitar la filtración de datos en la validación cruzada.

Para crear una tubería, debe proporcionar una lista de pares `(clave, valor)`, donde la `clave` es una cadena para identificar cada paso y el `valor` es un objeto estimador. A continuación, se muestra un ejemplo de creación de una tubería con un transformador PCA y un clasificador SVM:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

Puede acceder a los pasos de una tubería mediante indexación o por nombre:

```python
pipe.steps[0]  # acceso por índice
pipe[0]  # equivalente al anterior
pipe['reduce_dim']  # acceso por nombre
```

También puede usar la función `make_pipeline` como un atajo para la construcción de tuberías:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
