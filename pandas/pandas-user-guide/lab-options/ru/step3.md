# Сброс параметров

Если мы хотим сбросить один или несколько параметров до их значений по умолчанию, мы можем использовать `pd.reset_option`.

```python
# Reset the maximum display rows to default
pd.reset_option("display.max_rows")

# Verify the reset
print(pd.options.display.max_rows)
```
