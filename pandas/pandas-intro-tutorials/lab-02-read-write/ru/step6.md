# Чтение данных из Excel

Чтение данных из Excel-файла так же просто, как и чтение данных из CSV-файла. Мы будем использовать функцию `read_excel` из библиотеки pandas.

```python
# Чтение данных из Excel-файла
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
