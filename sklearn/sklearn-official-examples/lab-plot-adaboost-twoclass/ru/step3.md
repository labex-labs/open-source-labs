# Создаем и настраиваем AdaBoost-решательное дерево

В этом шаге мы создадим AdaBoost-решательное дерево с использованием класса `AdaBoostClassifier` из модуля `sklearn.ensemble`. В качестве базового оценивающего алгоритма мы будем использовать решательное дерево и установим параметр `max_depth` равным 1. Также установим параметр `algorithm` равным "SAMME" и параметр `n_estimators` равным 200. Наконец, настроим классификатор на наборе данных.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
