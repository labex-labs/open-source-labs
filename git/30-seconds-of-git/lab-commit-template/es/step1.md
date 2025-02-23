# Agregar una plantilla de mensaje de confirmación

Sin una plantilla de mensaje de confirmación, los desarrolladores pueden tener la tentación de escribir mensajes de confirmación vagos o sin información, como "arreglado error" o "código actualizado". Esto dificulta que otros entiendan el propósito del cambio y puede llevar a confusión o errores más adelante. Al configurar una plantilla de mensaje de confirmación, se anima a los desarrolladores a proporcionar mensajes de confirmación más detallados e informativos, lo que puede mejorar la colaboración y la productividad.

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Siga estos pasos para configurar una plantilla de mensaje de confirmación para este repositorio:

1. Clone el repositorio en su máquina local usando el comando `git clone https://github.com/labex-labs/git-playground`.
2. Navegue hasta el directorio del repositorio usando el comando `cd git-playground` y configure su cuenta de GitHub usando los comandos `git config --global user.name "su-nombre-de-usuario"` y `git config --global user.email "su-correo-electrónico"`.
3. Cree un nuevo archivo llamado `commit-template` en el directorio del repositorio usando el comando `vim commit-template`.
4. Abra el archivo `commit-template` en un editor de texto y agregue las siguientes líneas:

```shell
# <tipo>: <asunto>

# <cuerpo>

# <pie de página>

# Esto crea una plantilla con tres secciones, donde "<tipo>" indica el tipo de envío, como "func" o "arreglo", "<asunto>" es un resumen corto que describe el contenido del envío, "<cuerpo>" es una descripción más detallada y "<pie de página>" puede contener otros metadatos, como el número de problema asociado o otros comentarios.
```

5. Presione <kbd>Esc</kbd> y escriba el comando <kbd>:wq</kbd>, luego presione <kbd>Enter</kbd> para guardar sus cambios y salir del editor de archivos `commit-template`.
6. Use el comando `git add commit-template` para agregar los archivos `commit-template` a la área de preparación.
7. Use el comando `git config commit.template commit-template` para establecer el archivo `commit-template` como la plantilla de mensaje de confirmación para el repositorio.
8. Use el comando `git commit` para abrir el editor de mensaje de confirmación y observe que el editor de mensaje de confirmación ahora contiene la plantilla de mensaje de confirmación que creó en el paso 4.
9. Presione <kbd>Esc</kbd> y escriba el comando <kbd>:q</kbd>, luego presione <kbd>Enter</kbd> para salir del editor de mensaje de confirmación.
