# Introducción

**Objetivos:**

- Usar corrutinas para configurar tuberías de procesamiento

**Archivos creados:** `cofollow.py`, `coticker.py`

**Nota**

Para este ejercicio, el programa `stocksim.py` debe seguir ejecutándose en segundo plano.

En el Ejercicio 8.2 escribiste código que usaba generadores para configurar una tubería de procesamiento. Un aspecto clave de ese programa fue la idea de que los datos fluyen entre funciones generadoras. Se puede configurar un tipo de flujo de datos muy similar usando corrutinas. La única diferencia es que con una corrutina, se envían datos a diferentes elementos de procesamiento en lugar de extraerlos con un bucle for.
