# Создать данные для гистограммы

На этом этапе нам нужно создать данные для гистограммы. Мы будем использовать библиотеку numpy для создания массива значений, которые мы будем использовать для гистограммы.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
