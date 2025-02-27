# Подгонка регрессионной модели

Далее мы подгоняем модель SVR к нашему выборочному набору данных с использованием линейного, полиномиального и RBF-ядра. Мы настраиваем гиперпараметры для каждой модели и обучаем их на нашем выборочном наборе данных.

```python
from sklearn.svm import SVR

# Fit regression model
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
