# Git Cherry-Pick

Como desarrollador, estás trabajando en un proyecto con múltiples ramas. Has identificado un cambio específico que se realizó en un commit anterior que deseas aplicar a tu rama actual. Sin embargo, no deseas fusionar la rama completa ya que contiene otros cambios que no necesitas.

## Tareas

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio y configura la identidad.
2. Crea y cambia a una rama llamada `one-branch`, crea un archivo llamado `hello.txt`, escribe "hello,world" en él, agréguelo al área de preparación y confírmalo con el mensaje "add hello.txt".
3. Identifica el hash del commit creado en el paso anterior para aplicarlo a la rama `master`.
4. Haz checkout de la rama `master` y aplica el cambio a la rama `master`.
5. Verifica que el cambio se haya aplicado a la rama `master`.

Este es el resultado de ejecutar `git log` en la rama `master`:

```shell

ADD hello.txt
```
