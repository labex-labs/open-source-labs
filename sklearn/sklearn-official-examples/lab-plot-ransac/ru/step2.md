# Подберем линейную модель

Мы подберём линейную модель для данных с использованием класса LinearRegression из scikit-learn.

```python
# Fit line using all data
lr = linear_model.LinearRegression()
lr.fit(X, y)
```
