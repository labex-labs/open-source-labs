# Заменяем значения в столбце

Наконец, давайте заменим значения в столбце `Sex`: 'male' на 'M', а 'female' на 'F'. Для этого мы используем метод `replace()`.

```python
# Replace'male' with 'M' and 'female' with 'F' in the 'Sex' column
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
