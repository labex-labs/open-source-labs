# Обучение модели машинного обучения

Теперь, когда мы подготовили набор данных, мы можем обучить модель машинного обучения на обучающих данных. В этом примере мы будем использовать алгоритм Support Vector Machine (SVM):

```python
from sklearn.svm import SVC

# Create the SVM classifier
clf = SVC(kernel='linear')

# Train the classifier on the training data
clf.fit(X_train, y_train)
```
