# Настройка классификатора SVM

Мы настроим классификатор SVM с ядром радиальной базисной функции (RBF). SVM - это алгоритм обучения с учителем, который находит оптимальную гиперплоскость, которая разделяет данные на разные классы.

```python
from sklearn.svm import SVC

# Set up the SVM classifier
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC with rbf kernel")
```
