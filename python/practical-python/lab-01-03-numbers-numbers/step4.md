# Floating point (float)

Use a decimal or exponential notation to specify a floating point value:

```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```

Floats are represented as double precision using the native CPU representation [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
This is the same as the `double` type in the programming language C.

> 17 digits of precision  
> Exponent from -308 to 308

Be aware that floating point numbers are inexact when representing decimals.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

This is **not a Python issue**, but the underlying floating point hardware on the CPU.

Common Operations:

```
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value
```

These are the same operators as Integers, except for the bit-wise operators.
Additional math functions are found in the `math` module.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
