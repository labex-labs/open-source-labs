# Cerrando un generador

Una pregunta común sobre los generadores es su tiempo de vida y la recolección de basura. Por ejemplo, el generador `follow()` se ejecuta para siempre en un bucle `while` infinito. ¿Qué pasa si el bucle de iteración que lo impulsa se detiene? Además, ¿hay alguna manera de terminar prematuramente el generador?

Modifica la función `follow()` de modo que todo el código esté encerrado en un bloque `try-except` como este:

```python
def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                 line = f.readline()
                 if line == '':
                     time.sleep(0.1)    # Dormir brevemente para evitar espera activa
                     continue
                 yield line
    except GeneratorExit:
        print('Following Done')
```

Ahora, prueba algunos experimentos:

```python
>>> from follow import follow
>>> # Experiment: Recolección de basura de un generador en ejecución
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f
Following Done
>>> # Experiment: Cerrando un generador
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            f.close()

"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
...
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
        print(line, end='')    # Sin salida: el generador ha terminado

>>>
```

En estos experimentos se puede ver que se lanza una excepción `GeneratorExit` cuando un generador se recoge como basura o se cierra explícitamente a través de su método `close()`.

Una área adicional de exploración es si es posible reanudar la iteración en un generador si se sale de un bucle `for`. Por ejemplo, prueba esto:

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
...
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> # Reanudar la iteración
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
...
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
>>> del f
Following Done
>>>
```

En general, se puede salir de una iteración en ejecución y reanudarla más tarde si es necesario. Solo se debe asegurarse de que el objeto generador no se cierre forzosamente o se recoja como basura de alguna manera.
