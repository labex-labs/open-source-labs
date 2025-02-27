# Загрузка датасета и предобработка

Мы будем использовать библиотеку scikit-learn для загрузки датасета Iris. Датасет содержит 3 класса по 50 экземпляров каждый, где каждый класс относится к определенному типу ириса. Каждый экземпляр имеет 4 признака: длину и ширину чашелистика, длину и ширину лепестка.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target
```
