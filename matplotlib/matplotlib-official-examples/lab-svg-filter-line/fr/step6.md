# Définir un filtre

Nous définissons un filtre pour un flou gaussien en utilisant les balises `<defs>` et `<filter>` avec l'attribut `stdDeviation`.

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
