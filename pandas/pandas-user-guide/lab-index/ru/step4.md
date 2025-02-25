# Работа с пропущенными данными

Pandas предоставляет различные методы для очистки данных и заполнения пропущенных значений.

```python
# Creating a DataFrame with missing values
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Filling missing values
df.fillna(value=0, inplace=True)
```
