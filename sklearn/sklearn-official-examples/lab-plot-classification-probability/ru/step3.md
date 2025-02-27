# Определяем классификаторы

Определяем различные классификаторы для датасета.

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # для GPC

# Создаем разные классификаторы.
classifiers = {
    "L1 логистическая регрессия": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 логистическая регрессия (многочленная)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 логистическая регрессия (One-vs-Rest)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "Линейный SVC": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "GPC": GaussianProcessClassifier(kernel),
}
```
