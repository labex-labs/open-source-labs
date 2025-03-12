# Trabajando con números en Python

Python ofrece un sólido soporte para operaciones numéricas. En programación, los números son tipos de datos fundamentales utilizados para realizar cálculos y representar cantidades. Este paso te introducirá a la manipulación básica de números en Python, lo cual es esencial para realizar diversas operaciones matemáticas en tus programas.

## Operaciones aritméticas básicas

Para comenzar a trabajar con números en Python, primero debes abrir una shell interactiva de Python. Puedes hacer esto escribiendo `python3` en tu terminal. La shell interactiva de Python te permite escribir y ejecutar código Python línea por línea, lo cual es excelente para probar y aprender.

```bash
python3
```

Una vez que estés en la shell interactiva de Python, puedes probar algunas operaciones aritméticas básicas. Python sigue las reglas matemáticas estándar para la aritmética, como el orden de las operaciones (PEMDAS: Paréntesis, Exponentes, Multiplicación y División, Suma y Resta).

```python
>>> 3 + 4*5    # La multiplicación tiene mayor precedencia que la suma, por lo que se calcula 4*5 primero y luego se suma a 3
23
>>> 23.45 / 1e-02    # Aquí se utiliza la notación científica para 0.01. Se realiza la división para obtener el resultado
2345.0
```

## División entera

Python 3 maneja la división de manera diferente a Python 2. Comprender estas diferencias es crucial para evitar resultados inesperados en tu código.

```python
>>> 7 / 4    # En Python 3, la división regular devuelve un número de punto flotante (float), incluso si el resultado podría ser un entero
1.75
>>> 7 // 4   # La división entera (trunca la parte decimal) te da el cociente como un entero
1
```

## Métodos de números

Los números en Python tienen varios métodos útiles que a menudo se pasan por alto. Estos métodos pueden simplificar operaciones numéricas complejas y conversiones. Exploremos algunos de ellos:

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # Este método representa el número de punto flotante como una fracción, lo cual puede ser útil para algunos cálculos matemáticos
(2345, 2)
>>> x.is_integer()    # Comprueba si el número de punto flotante es un valor entero. En este caso, 1172.5 no es un entero, por lo que devuelve False
False

>>> y = 12345
>>> y.numerator    # Para los enteros, el numerador es el número mismo
12345
>>> y.denominator    # Para los enteros, el denominador siempre es 1
1
>>> y.bit_length()    # Este método te dice el número de bits necesarios para representar el número en binario, lo cual puede ser útil en operaciones bit a bit
14
```

Estos métodos son particularmente útiles cuando necesitas realizar operaciones numéricas específicas o conversiones. Pueden ahorrarte tiempo y hacer que tu código sea más eficiente.

Cuando hayas terminado de explorar la shell interactiva de Python, puedes salir de ella escribiendo:

```python
>>> exit()
```
