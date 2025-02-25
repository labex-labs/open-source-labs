# Использование пропущенных и заполняемых значений

Аргументы `missing_values` и `filling_values` используются для обработки пропущенных данных. Аргумент `missing_values` используется для распознавания пропущенных данных, а аргумент `filling_values` используется для предоставления значения для пропущенных записей.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
