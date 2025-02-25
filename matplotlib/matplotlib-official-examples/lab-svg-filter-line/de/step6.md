# Filter definieren

Wir definieren einen Filter für einen Gaußschen Verblendungseffekt mit den `<defs>`- und `<filter>`-Tags und dem `stdDeviation`-Attribut.

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
