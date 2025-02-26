# Desafío de análisis de datos

En la última práctica escribiste código para leer datos CSV relacionados con la Autoridad de Transporte de Chicago. Por ejemplo, puedes obtener los datos como diccionarios de la siguiente manera:

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>>
```

Sería una lástima hacer todo ese trabajo y luego no hacer nada con los datos.

En este ejercicio, tu tarea es la siguiente: escribe un programa para responder a las siguientes cuatro preguntas:

1. ¿Cuántas rutas de autobús hay en Chicago?

2. ¿Cuántas personas tomaron el autobús número 22 el 2 de febrero de 2011? ¿Y qué tal para cualquier ruta en cualquier fecha que elijas?

3. ¿Cuál es el número total de viajes realizados en cada ruta de autobús?

4. ¿Qué cinco rutas de autobús tuvieron el mayor aumento en el número de pasajeros en los últimos diez años, de 2001 a 2011?

Estás libre de utilizar cualquier técnica para responder a las preguntas anteriores siempre y cuando forme parte de la biblioteca estándar de Python (es decir, tipos de datos integrados, módulos de la biblioteca estándar, etc.).
