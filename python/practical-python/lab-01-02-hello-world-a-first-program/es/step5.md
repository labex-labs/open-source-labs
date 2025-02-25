# Un programa de ejemplo

Vamos a resolver el siguiente problema:

> Una mañana, sales y dejas un billete de dólar en la acera del Sears Tower en Chicago. A partir de entonces, cada día sales y dobles el número de billetes. ¿Cuánto tiempo tarda en que la pila de billetes supere la altura de la torre?

A continuación, se presenta una solución para crear un archivo `sears.py` en el directorio `/home/labex/project`:

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Metros (0.11 mm)
sears_height = 442 # Altura (metros)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Cuando lo ejecutas, obtienes la siguiente salida:

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Number of days 23
Number of bills 4194304
Final height 461.37344
```

Usando este programa como guía, puedes aprender una serie de conceptos básicos importantes sobre Python.
