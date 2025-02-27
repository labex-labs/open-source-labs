# Создание объекта последовательного случайного поиска

Создайте объект `HalvingRandomSearchCV` для поиска по пространству параметров. Объект принимает следующие аргументы:

- `estimator`: оцениваемая модель, которую нужно оптимизировать
- `param_distributions`: пространство параметров для поиска
- `factor`: коэффициент, на который количество кандидатов уменьшается на каждой итерации
- `random_state`: случайное состояние, используемое для поиска

Код для создания объекта выглядит следующим образом:

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
