# Atascado en el autobús

El archivo `ctabus.csv` es un archivo CSV que contiene datos diarios de pasajeros del sistema de autobuses de la Autoridad de Transporte de Chicago (CTA) desde el 1 de enero de 2001 hasta el 31 de agosto de 2013. Contiene aproximadamente 577000 filas de datos. Utilice Python para ver algunas líneas de datos para ver cómo se ven:

```python
>>> f = open('/home/labex/project/ctabus.csv')
>>> next(f)
'route,date,daytype,rides\n'
>>> next(f)
'3,01/01/2001,U,7354\n'
>>> next(f)
'4,01/01/2001,U,9288\n'
>>>
```

Hay 4 columnas de datos.

- route: Columna 0. El nombre de la ruta del autobús.
- date: Columna 1. Una cadena de fecha en el formato MM/DD/YYYY.
- daytype: Columna 2. Un código de tipo de día (U=Domingo/Feriado, A=Sábado, W=Día laboral)
- rides: Columna 3. Número total de pasajeros (entero)

La columna `rides` registra el número total de personas que subieron a un autobús en esa ruta en un día determinado. Por lo tanto, del ejemplo, 7354 personas tomaron el autobús número 3 el 1 de enero de 2001.
