# Настройка преобразования

Аргумент `converters` позволяет определить функции преобразования для обработки более сложных преобразований. Он принимает словарь, в котором ключами являются индексы столбцов или имена столбцов, а значениями — функции преобразования.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
