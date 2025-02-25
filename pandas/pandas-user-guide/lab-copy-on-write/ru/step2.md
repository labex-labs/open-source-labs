# Понимание Copy-On-Write с DataFrame

Теперь давайте создадим DataFrame и посмотрим, как CoW влияет на модификацию данных.

```python
# Создаем DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Создаем подмножество DataFrame
subset = df["foo"]

# Изменяем подмножество
subset.iloc[0] = 100

# Выводим исходный DataFrame
print(df)
```

## Реализация Copy-On-Write с DataFrame

Теперь давайте посмотрим, как реализовать CoW при изменении DataFrame.

```python
# Включаем CoW
pd.options.mode.copy_on_write = True

# Создаем подмножество DataFrame
subset = df["foo"]

# Изменяем подмножество
subset.iloc[0] = 100

# Выводим исходный DataFrame
print(df)
```
