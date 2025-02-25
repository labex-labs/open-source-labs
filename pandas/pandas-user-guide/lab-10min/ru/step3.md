# Создание DataFrame

Мы можем создать `DataFrame`, передав массив numpy, с индексом datetime и именованными столбцами.

```python
# Creating a pandas dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
