# Ejecutar bajo el depurador

También puedes ejecutar todo un programa bajo el depurador.

```bash
$ python3 -m pdb someprogram.py
```

Automáticamente entrará al depurador antes de la primera instrucción. Lo que te permite establecer puntos de ruptura y cambiar la configuración.

Comandos comunes del depurador:

```code
(Pdb) help            # Obtener ayuda
(Pdb) w(here)         # Imprimir la traza de pila
(Pdb) d(own)          # Moverse un nivel hacia abajo en la pila
(Pdb) u(p)            # Moverse un nivel hacia arriba en la pila
(Pdb) b(reak) loc     # Establecer un punto de ruptura
(Pdb) s(tep)          # Ejecutar una instrucción
(Pdb) c(ontinue)      # Continuar la ejecución
(Pdb) l(ist)          # Listar el código fuente
(Pdb) a(rgs)          # Imprimir los argumentos de la función actual
(Pdb)!statement      # Ejecutar una instrucción
```

Para los puntos de ruptura, la ubicación puede ser una de las siguientes.

```code
(Pdb) b 45            # Línea 45 en el archivo actual
(Pdb) b file.py:45    # Línea 45 en file.py
(Pdb) b foo           # Función foo() en el archivo actual
(Pdb) b module.foo    # Función foo() en un módulo
```
