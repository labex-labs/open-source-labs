# Извлекаем конкретные данные о пассажирах

Далее извлечем данные о пассажирах, которые были графинями на Титанике. Мы используем метод `str.contains()`, чтобы найти строки, в которых столбец `Name` содержит слово 'Countess'.

```python
# Find rows where 'Name' contains 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
