# Настройка классификаторов Self-training

Мы настроим два классификатора Self-training с разными процентами помеченных данных: 30% и 50%. Self-training - это алгоритм полуподдерживаемого обучения, который обучает классификатор на помеченных данных и затем использует его для предсказания меток не помеченных данных. Самые уверенные предсказания добавляются в помеченные данные, и процесс повторяется до сходимости.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Set up the Self-training classifiers
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% data",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% data",
)
```
