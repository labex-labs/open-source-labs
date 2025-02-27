# Вычисление пути Lasso

Далее мы вычисляем путь Lasso с использованием алгоритма LARS. Функция `lars_path` из модуля `linear_model` Scikit-Learn используется для вычисления пути Lasso. Функция принимает входные признаки, целеевую переменную и метод в качестве параметров. В этом случае мы используем метод "lasso" для L1-регуляризации.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
