# Agregar una plantilla de mensaje de confirmación

Sin una plantilla de mensaje de confirmación, los desarrolladores pueden tener la tentación de escribir mensajes de confirmación vagos o sin información, como "arreglado error" o "código actualizado". Esto dificulta que otros entiendan el propósito del cambio y puede llevar a confusión o errores más adelante. Al configurar una plantilla de mensaje de confirmación, se anima a los desarrolladores a proporcionar mensajes de confirmación más detallados e informativos, lo que puede mejorar la colaboración y la productividad.

## Tareas

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navegue hasta el directorio del repositorio y configure su identidad de GitHub.
2. Cree un nuevo archivo llamado `commit-template` en el directorio actual del repositorio.
3. Abra el archivo `commit-template` en un editor de texto y agregue las siguientes líneas:

```shell
# <tipo>: <asunto>

# <cuerpo>

# <pie de página>

# Esto crea una plantilla con tres secciones:
# "<tipo>" indica el tipo de envío, como "func" o "arreglo"
# "<asunto>" es un resumen corto que describe el contenido del envío
# "<cuerpo>" es una descripción más detallada
# "<pie de página>" puede contener otros metadatos, como el número de problema asociado o otros comentarios.
```

4. Presione <kbd>Esc</kbd> y escriba el comando <kbd>:wq</kbd>, luego presione <kbd>Enter</kbd> para guardar sus cambios y salir del editor de archivos `commit-template`.
5. Agregue los archivos `commit-template` al área de preparación.
6. Establezca el archivo `commit-template` como la plantilla de mensaje de confirmación para el repositorio.
7. Abra el editor de mensaje de confirmación y observe que el editor de mensaje de confirmación ahora contiene la plantilla de mensaje de confirmación que creó en el paso 3.
8. Presione <kbd>Esc</kbd> y escriba el comando <kbd>:q</kbd>, luego presione <kbd>Enter</kbd> para salir del editor de mensaje de confirmación.
