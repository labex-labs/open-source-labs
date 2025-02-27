# Рекурсивное исключение признаков

Рекурсивное исключение признаков (Recursive Feature Elimination, RFE) - это метод выбора признаков, который последовательно рассматривает все более мелкие наборы признаков для выбора наиболее важных. Он работает путём обучения внешнего оценивателя с весами, присвоенными признакам, и удалением наименее важных признаков.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SVC as the external estimator
estimator = SVC(kernel="linear")

# Initialize RFE with the external estimator and select 2 features
selector = RFE(estimator, n_features_to_select=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

В этом примере мы используем классификатор на основе векторов опор (Support Vector Classifier, SVC) в качестве внешнего оценивателя и выбираем два наилучших признака из набора данных Iris. Вывод покажет исходную форму набора данных и форму после выбора наилучших признаков.
