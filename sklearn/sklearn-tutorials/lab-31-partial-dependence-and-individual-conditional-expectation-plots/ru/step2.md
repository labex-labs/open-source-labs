# Загружаем и готовим данные

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Создаем DataFrame для более удобной манипуляции данными
df = pd.DataFrame(X, columns=feature_names)
```
