# Copiar un archivo de otra rama

Estás trabajando en un proyecto en un repositorio de Git llamado `https://github.com/labex-labs/git-playground.git`. Tienes dos ramas llamadas `feature-1` y `feature-2`. Necesitas copiar el archivo `hello.txt` de la rama `feature-1` a la rama `feature-2`.

## Tareas

1. Navega hasta el directorio y configura la identidad.
2. Crea y cambia a la rama `feature-1` y crea un archivo de texto llamado `hello.txt` y escribe la cadena "hello,world" en él y confirma el archivo con el mensaje "add hello.txt".
3. Crea y cambia a la rama `feature-2` después de cambiar a la rama `master`.
4. Copia el archivo `hello.txt` de la rama `feature-1` a la rama `feature-2` y confirma con el mensaje de confirmación "copy hello.txt".
5. Verifica que el archivo `hello.txt` se haya copiado a la rama `feature-2`.

Deberías ver el archivo `hello.txt` en la lista de archivos de la rama `feature-2`:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
