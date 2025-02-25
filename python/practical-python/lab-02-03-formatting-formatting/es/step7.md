# Ejercicio 2.9: Recopilando datos

En el Ejercicio 2.7, escribiste un programa llamado `report.py` que calculaba la ganancia/perdida de una cartera de acciones. En este ejercicio, vas a comenzar a modificarlo para generar una tabla como esta:

          Nombre     Acciones      Precio     Cambio
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

En este informe, "Precio" es el precio actual de la acción y "Cambio" es el cambio en el precio de la acción desde el precio de compra inicial.

Para generar el informe anterior, primero querrás recopilar todos los datos mostrados en la tabla. Escribe una función `make_report()` que tome una lista de acciones y un diccionario de precios como entrada y devuelva una lista de tuplas que contengan las filas de la tabla anterior.

Agrega esta función a tu archivo `report.py`. Aquí es cómo debería funcionar si la pruebas interactiva:

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> report = make_report(portfolio, prices)
>>> for r in report:
        print(r)

('AA', 100, 9.22, -22.980000000000004)
('IBM', 50, 106.28, 15.180000000000007)
('CAT', 150, 35.46, -47.98)
('MSFT', 200, 20.89, -30.339999999999996)
('GE', 95, 13.48, -26.889999999999997)
...
>>>
```
