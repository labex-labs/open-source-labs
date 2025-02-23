# Configurar los finales de línea

Estás trabajando en un proyecto con un equipo de desarrolladores y notas que algunos miembros del equipo están utilizando diferentes finales de línea que otros. Esto puede causar problemas al fusionar el código y puede llevar a conflictos. Necesitas configurar los finales de línea para el repositorio para garantizar la consistencia y evitar conflictos.

En sistemas Unix o similares, cada línea de texto termina con el terminador de línea `LF` (Line Feed). Cuando utilizas el comando `cat` para ver un archivo, los terminadores de línea normalmente no se muestran en la pantalla porque se consideran el final de la línea, no parte de la línea.

Al ver un archivo con el comando `cat -vet`, la opción `-v` muestra los caracteres no imprimibles como secuencias de caracteres visibles, como el símbolo `$`. Por lo tanto, si ves el símbolo `$` en un archivo, significa que cada línea del archivo termina con el terminador de línea `LF`. `LF` y `\n` son el mismo concepto, que indica un terminador de línea.

Para configurar los finales de línea para el repositorio `git-playground`, sigue estos pasos:

1. Abre la línea de comandos o la terminal de tu computadora.
2. Navega hasta el directorio donde se encuentra el repositorio `git-playground` en el directorio `~/project`.
3. Ejecuta el siguiente comando para configurar los finales de línea para utilizar finales de línea UNIX:

   ```shell
   git config core.eol lf
   ```

   Esto configurará los finales de línea para utilizar el final de línea UNIX (`\n`).

4. Ejecuta el siguiente comando para verificar que los finales de línea se han configurado correctamente:

   ```shell
   git config core.eol
   ```

   Esto mostrará la configuración actual de los finales de línea.

Este es el resultado de ejecutar `cat -vet file2.txt`:

```shell
This is file2.$
```
