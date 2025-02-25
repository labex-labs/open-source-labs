# Понимание последствий наличия дубликатов меток

Дубликаты меток могут изменить поведение некоторых операций в pandas. Например, некоторые методы не работают, если есть дубликаты.

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
