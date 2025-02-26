# Problema: Scripts Principales

Ejecutar un submódulo de un paquete como un script principal se rompe.

```bash
$ python porty/pcost.py # SE ROMPE
...
```

_Razón: Estás ejecutando Python en un solo archivo y Python no ve correctamente el resto de la estructura del paquete (`sys.path` está incorrecto)._

Todas las importaciones se rompen. Para solucionar esto, debes ejecutar tu programa de una manera diferente, usando la opción `-m`.

```bash
$ python -m porty.pcost # FUNCIONA
...
```
