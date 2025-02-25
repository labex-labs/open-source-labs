# Запись данных в Excel

Вы также можете записать данные в Excel-файл, используя метод `to_excel`. Сохраним наш DataFrame в Excel-файл.

```python
# Сохранение DataFrame в Excel-файл
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
