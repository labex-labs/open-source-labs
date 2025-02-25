# Establecer el localizador y formateador de marcas

Se utilizará la función RRuleLocator para establecer el localizador de marcas basado en la regla de recurrencia que se estableció en el paso anterior. También se utilizará la función DateFormatter para establecer el formateador de marcas.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```
