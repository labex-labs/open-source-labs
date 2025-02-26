# Ejercicio 7.1: Un ejemplo simple de argumentos variables

Intenta definir la siguiente función:

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

Observa cómo el parámetro `*more` recopila todos los argumentos adicionales.
