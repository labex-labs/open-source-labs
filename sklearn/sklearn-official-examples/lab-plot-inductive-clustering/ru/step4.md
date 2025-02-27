# Объявление модели индуктивного обучения

В этом шаге мы объявим модель индуктивного обучения, которая будет использоваться для предсказания принадлежности кластера для неизвестных экземпляров. В качестве классификатора мы будем использовать `RandomForestClassifier` из scikit-learn.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```
