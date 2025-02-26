# Leyendo un portafolio

Agrega una función `read_portfolio()` a tu programa `stock.py` que lea un archivo de datos de portafolio en una lista de objetos `Stock`. Así es como debería funcionar:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

Ya escribiste una función similar como parte del Ejercicio 2.3. Discusión de diseño: ¿Debería `read_portfolio()` ser una función separada o parte de la definición de clase?

## Nota:

Agrega la función `read_portfolio()` en el archivo `stock.py`.
