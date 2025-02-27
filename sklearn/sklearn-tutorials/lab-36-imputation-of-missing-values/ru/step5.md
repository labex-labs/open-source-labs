# Сохранение постоянного числа признаков

По умолчанию, импутаторы scikit-learn удаляют столбцы, содержащие только пропущенные значения. Однако, в некоторых случаях необходимо сохранить пустые признаки, чтобы сохранить форму данных. Мы можем это сделать, установив параметр `keep_empty_features` в значение True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
