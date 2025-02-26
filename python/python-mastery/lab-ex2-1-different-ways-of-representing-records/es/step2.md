# Uso básico de memoria de texto

Vamos a obtener una línea base de la memoria requerida para trabajar con este archivo de datos. Primero, reinicie Python y pruebe un experimento muy simple de simplemente tomar el archivo y almacenar sus datos en una sola cadena:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

Sus resultados pueden variar un poco, pero debería ver que el uso actual de memoria está en el rango de 12MB con un pico de 24MB.

¿Qué pasa si lee todo el archivo en una lista de cadenas en su lugar? Reinicie Python y pruebe esto:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

Debería ver que el uso de memoria aumenta significativamente hasta el rango de 40-50MB. Punto para reflexionar: ¿cuál podría ser la fuente de ese costo adicional?
