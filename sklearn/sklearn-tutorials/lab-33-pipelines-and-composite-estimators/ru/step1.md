# Конвейер - последовательное соединение оценщиков

Класс `Pipeline` в scikit-learn используется для последовательного соединения нескольких оценщиков в один. Это позволяет вызывать методы `fit` и `predict` один раз для своих данных, чтобы обучить целый ряд оценщиков. Также позволяет выбирать параметры совместно и помогает избежать утечки данных при кросс-валидации.

Для создания конвейера необходимо передать список пар `(ключ, значение)`, где `ключ` - это строка для идентификации каждого шага, а `значение` - это объект оценщика. Ниже приведен пример создания конвейера с трансформером PCA и классификатором SVM:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

Вы можете получить доступ к шагам конвейера с использованием индексации или по имени:

```python
pipe.steps[0]  # доступ по индексу
pipe[0]  # эквивалентно предыдущему
pipe['reduce_dim']  # доступ по имени
```

Также можно использовать функцию `make_pipeline` в качестве сокращения для построения конвейеров:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
