# Загрузка данных

Далее мы загрузим набор данных ирисов (iris dataset) из библиотеки scikit-learn. Этот набор данных является классическим набором данных для машинного обучения, который состоит из измерений ирисов и меток их видов.

```python
iris = load_iris()
X = iris.data
y = iris.target
```
