# Загрузка набора данных Iris и разделение данных

Мы загрузим набор данных Iris, который широко используется в машинном обучении для задач классификации. В наборе данных содержится 150 образцов цветов Ириса, и для каждого образца четыре признака: длина чашелистика, ширина чашелистика, длина лепестка и ширина лепестка. Мы разделим набор данных на входные признаки и целевые метки.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into input features and target labels
X = iris.data[:, :2] # We will only use the first two features for visualization purposes
y = iris.target
```
