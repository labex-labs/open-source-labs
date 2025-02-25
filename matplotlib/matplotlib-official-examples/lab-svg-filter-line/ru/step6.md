# Определяем фильтр

Мы определяем фильтр для гауссовского размытия с использованием тегов `<defs>` и `<filter>` с атрибутом `stdDeviation`.

```python
filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""
```
