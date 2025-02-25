# Ejercicio 1.6: Depuración

El siguiente fragmento de código contiene código del problema de la torre Sears. También tiene un error en él.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Metros (0.11 mm)
sears_height   = 442             # Altura (metros)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Copie y pegue el código que aparece arriba en un nuevo programa llamado `sears.py`. Cuando ejecute el código, obtendrá un mensaje de error que hará que el programa se detenga así:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Leer los mensajes de error es una parte importante del código de Python. Si su programa se detiene, la última línea del mensaje de seguimiento es la razón real por la que el programa se detuvo. Por encima de eso, debería ver un fragmento de código fuente y luego un nombre de archivo identificador y un número de línea.

- ¿Qué línea es el error?
- ¿Cuál es el error?
- Corrija el error
- Ejecute el programa correctamente
