# Ponto flutuante (float)

Use notação decimal ou exponencial para especificar um valor de ponto flutuante:

```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```

Floats são representados como precisão dupla usando a representação nativa da CPU [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). Esta é a mesma que o tipo `double` na linguagem de programação C.

> 17 dígitos de precisão\
> Expoente de -308 a 308

Esteja ciente de que números de ponto flutuante são inexatos ao representar decimais.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Este **não é um problema do Python**, mas sim do hardware de ponto flutuante subjacente na CPU.

Operações comuns:

    x + y      Adição (Add)
    x - y      Subtração (Subtract)
    x * y      Multiplicação (Multiply)
    x / y      Divisão (Divide)
    x // y     Divisão inteira (Floor Divide)
    x % y      Módulo (Modulo)
    x ** y     Potência (Power)
    abs(x)     Valor absoluto (Absolute Value)

Estes são os mesmos operadores que os Inteiros, exceto pelos operadores bit a bit. Funções matemáticas adicionais são encontradas no módulo `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
