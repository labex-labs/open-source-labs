# Построение кривых частичной зависимости для двух признаков

В этом шаге мы построим кривые частичной зависимости для признаков "возраст" и "ИМТ" (индекс массы тела) для дерева решений. При наличии двух признаков функция `PartialDependenceDisplay.from_estimator` ожидает построения двух кривых. Здесь функция построения создает сетку из двух графиков, используя пространство, определенное параметром `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

Можно построить кривые частичной зависимости для многослойного перцептрона. В этом случае параметр `line_kw` передается в функцию `PartialDependenceDisplay.from_estimator`, чтобы изменить цвет кривой.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
