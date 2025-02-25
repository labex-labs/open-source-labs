# Создание DataFrame

Другая фундаментальная структура данных — это DataFrame. Это двухмерная структура данных с метками, в которой столбцы могут иметь разные типы.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
