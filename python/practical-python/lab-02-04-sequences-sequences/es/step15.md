# Ejercicio 2.16: Usando la función zip()

En el archivo `portfolio.csv`, la primera línea contiene los encabezados de columna. En todo el código anterior, los hemos estado descartando.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>>
```

Sin embargo, ¿y si pudieras usar los encabezados para algo útil? Aquí es donde entra en juego la función `zip()`. Primero, intenta esto para emparejar los encabezados del archivo con una fila de datos:

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Observa cómo `zip()` empareja los encabezados de columna con los valores de columna. Aquí hemos usado `list()` para convertir el resultado en una lista para que puedas verlo. Normalmente, `zip()` crea un iterador que debe ser consumido por un bucle `for`.

Esta emparejamiento es un paso intermedio para construir un diccionario. Ahora, intenta esto:

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Esta transformación es uno de los trucos más útiles de los que debes saber cuando estás procesando muchos archivos de datos. Por ejemplo, supongamos que quisieras hacer que el programa `pcost.py` funcione con varios archivos de entrada, pero sin importar el número real de columna donde aparecen el nombre, las acciones y el precio.

Modifica la función `portfolio_cost()` en `pcost.py` de modo que se vea así:

```python
# pcost.py

def portfolio_cost(filename):
 ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # Esto captura errores en las conversiones de int() y float() anteriores
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
     ...
```

Ahora, prueba tu función en un archivo de datos completamente diferente `portfoliodate.csv` que se ve así:

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

Si lo hiciste correctamente, encontrarás que tu programa todavía funciona aunque el archivo de datos tiene un formato de columna completamente diferente al anterior. ¡Eso es genial!

El cambio realizado aquí es sutil, pero significativo. En lugar de que `portfolio_cost()` esté codificado para leer un solo formato de archivo fijo, la nueva versión lee cualquier archivo CSV y extrae los valores de interés de él. Siempre que el archivo tenga las columnas requeridas, el código funcionará.

Modifica el programa `report.py` que escribiste en la Sección 2.3 de modo que use la misma técnica para extraer los encabezados de columna.

Intenta ejecutar el programa `report.py` en el archivo `portfoliodate.csv` y verifica que produzca la misma respuesta que antes.
