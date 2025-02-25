# Преобразуем символы строки в нижний регистр

Далее мы преобразуем все символы в столбце `Name` в нижний регистр. Для этого мы используем метод `str.lower()`.

```python
# Convert all characters in the 'Name' column to lowercase
titanic["Name"] = titanic["Name"].str.lower()
```
