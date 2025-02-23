# Autocorrect Git Commands

El problema es que los desarrolladores a menudo escriben mal los comandos de git, lo que puede causar errores y ralentizar su flujo de trabajo. Por ejemplo, un desarrollador podría accidentalmente escribir `git sttaus` en lugar de `git status`, lo que resultará en un mensaje de error. Esto puede ser frustrante y consume tiempo, especialmente cuando se trabaja en grandes proyectos con muchos archivos y colaboradores.

Para demostrar cómo usar la característica de autocorrección de Git, usaremos el repositorio de git llamado `https://github.com/labex-labs/git-playground` en el directorio.

1. Abra su terminal y navegue hasta el directorio donde desea clonar el repositorio.
2. Clone el repositorio usando el siguiente comando:

```
git clone https://github.com/labex-labs/git-playground.git
```

3. Navegue hasta el repositorio clonado usando el siguiente comando:

```
cd git-playground
```

4. Habilite la característica de autocorrección de Git usando el siguiente comando:

```
git config --global help.autocorrect 1
```

5. Intente escribir mal un comando de git, como `git sttaus`. Git automáticamente corregirá el comando y ejecutará `git status` en su lugar.

Este es el resultado después de completar el laboratorio:

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
