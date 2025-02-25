# Punto flotante (float)

Utilice notación decimal o exponencial para especificar un valor de punto flotante:

```python
a = 37.45
b = 4e5 # 4 x 10**5 o 400,000
c = -1.345e-10
```

Los floats se representan con doble precisión utilizando la representación nativa de la CPU [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). Esto es lo mismo que el tipo `double` en el lenguaje de programación C.

> 17 dígitos de precisión\
> Exponente de -308 a 308

Tenga en cuenta que los números de punto flotante son imprecisos al representar decimales.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Esto **no es un problema de Python**, sino el hardware de punto flotante subyacente en la CPU.

Operaciones comunes:

    x + y      Sumar
    x - y      Restar
    x * y      Multiplicar
    x / y      Dividir
    x // y     Dividir hacia abajo
    x % y      Módulo
    x ** y     Potencia
    abs(x)     Valor Absoluto

Estos son los mismos operadores que los enteros, excepto los operadores bit a bit. Funciones matemáticas adicionales se encuentran en el módulo `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
