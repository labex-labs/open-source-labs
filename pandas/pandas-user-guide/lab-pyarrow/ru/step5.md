# Операции с PyArrow

Интеграция структуры данных PyArrow реализуется через интерфейс ExtensionArray pandas. Поддерживаемая функциональность существует там, где этот интерфейс интегрирован в API pandas.

```python
# Создать pandas Series с типом данных PyArrow
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Выполнить различные операции
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
