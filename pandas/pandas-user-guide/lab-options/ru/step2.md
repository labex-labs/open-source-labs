# Получение и настройка параметров

Мы можем получить или установить значение одного параметра с использованием `pd.get_option` или `pd.set_option` соответственно. Здесь мы устанавливаем максимальное количество отображаемых строк в 999.

```python
# Get the current setting for maximum display rows
print(pd.options.display.max_rows)

# Set the maximum display rows to 999
pd.options.display.max_rows = 999

# Verify the new setting
print(pd.options.display.max_rows)
```
