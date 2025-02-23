# Crea un nuevo repositorio

Hemos aprendido cómo clonar un repositorio Git existente. Ahora, creemos un nuevo repositorio Git desde cero.

Abre tu terminal o línea de comandos y sigue los pasos siguientes para crear un nuevo repositorio Git:

```bash
cd ~/project
git init my_repo
```

Esto creará un nuevo directorio llamado `my_repo` en tu directorio de trabajo actual e inicializará un nuevo repositorio Git dentro de él.

Veamos qué hay dentro del directorio `my_repo`:

```bash
ls -a my_repo
```

Deberías ver los siguientes archivos y directorios:

```plaintext
. .. .git
```

Los directorios `.` y `..` son directorios especiales que representan el directorio actual y el directorio padre, respectivamente.

El directorio `.git` es donde Git almacena todos los archivos de configuración y el historial de versiones del repositorio.

Intenta ejecutar el siguiente comando para ver los archivos y directorios dentro del directorio `.git`:

```bash
ls -a my_repo/.git
```

Deberías ver los siguientes archivos y directorios:

```plaintext
. ..  branches  config  description  HEAD  hooks  info  objects  ref
```

- El directorio `branches` contiene referencias a las ramas del repositorio.
- El archivo `config` contiene los ajustes de configuración específicos del repositorio.
- El archivo `description` contiene una breve descripción del repositorio.
- El archivo `HEAD` contiene una referencia a la rama actualmente seleccionada.
- El directorio `hooks` contiene scripts que pueden ser desencadenados por eventos de Git.
- El directorio `info` contiene archivos de información global.
- El directorio `objects` contiene todos los objetos del repositorio.
- El directorio `ref` contiene referencias a los commits del repositorio.

No necesitamos preocuparnos por el contenido del directorio `.git` por ahora. Simplemente recuerda que es donde Git almacena toda la información sobre el repositorio.
