# Definir Filtro

Definimos um filtro para um desfoque Gaussiano usando as tags `<defs>` e `<filter>` com o atributo `stdDeviation`.

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
