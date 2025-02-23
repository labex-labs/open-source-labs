# Extracción de todos los submódulos desde el remoto

Tienes un repositorio de Git con submódulos que deben actualizarse desde sus respectivos remotos. Extraer manualmente cada submódulo puede ser tedioso y propenso a errores. Necesitas una forma de extraer todos los submódulos a la vez.

Asumiendo que tienes un repositorio de Git llamado `git` que contiene submódulos, puedes extraer todos los submódulos de sus respectivos remotos utilizando el siguiente comando:

```shell
cd git
git submodule update --recursive --remote
```

Este comando actualiza todos los submódulos del repositorio a la última versión disponible en sus respectivos remotos.
