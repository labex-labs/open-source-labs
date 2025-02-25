# Найдем самое длинное имя

Посмотрим, какой пассажир Титаника имеет самое длинное имя. Мы используем метод `str.len()`, чтобы получить длину каждого имени, и метод `idxmax()`, чтобы найти индекс самого длинного имени.

```python
# Get the length of each name
name_lengths = titanic["Name"].str.len()

# Find the index of the longest name
longest_name_index = name_lengths.idxmax()

# Get the longest name
longest_name = titanic.loc[longest_name_index, "Name"]
```
