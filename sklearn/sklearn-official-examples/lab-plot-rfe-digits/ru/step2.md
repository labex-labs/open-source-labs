# Создание объекта RFE и подгонка данных

Далее мы создадим объект класса RFE и подгоним к нему данные. В качестве оценщика мы будем использовать классификатор на основе векторов поддержки (Support Vector Classifier, SVC) с линейным ядром. Мы будем выбирать по одному признаку за раз и делать по одному шагу за раз.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
