# Использование option_context

Функция `option_context` позволяет нам выполнить блок кода с набором параметров, которые возвращаются к предыдущим настройкам после выполнения.

```python
# Execute a code block with a set of options
with pd.option_context("display.max_rows", 10):
    # This will print 10 despite the global setting being different
    print(pd.get_option("display.max_rows"))

# This will print the global setting as the context block has ended
print(pd.get_option("display.max_rows"))
```
