# Параметры оценщиков

Объекты оценщиков могут иметь параметры, влияющие на их поведение. Эти параметры можно задавать при инициализации оценщика или путём изменения соответствующего атрибута. Зададим несколько параметров для нашего примера оценщика:

```python
estimator = Estimator(param1=1, param2=2)
print(estimator.param1)
```

Результат:

```
1
```
