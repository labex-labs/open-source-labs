# Ejercicio 3.2: Crear una función de nivel superior para la ejecución del programa

Toma la última parte de tu programa y encapsúlala en una función única `portfolio_report(portfolio_filename, prices_filename)`. Haz que la función funcione de modo que la siguiente llamada a la función cree el informe como antes:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

En esta versión final, tu programa no será más que una serie de definiciones de funciones seguidas de una única llamada a la función `portfolio_report()` al final (que ejecuta todos los pasos involucrados en el programa).

Al convertir tu programa en una única función, se vuelve fácil ejecutarlo con diferentes entradas. Por ejemplo, prueba estas declaraciones de manera interactiva después de ejecutar tu programa:

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... mira la salida...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... mira la salida...
>>>
```
