# Instalar el proyecto

A continuación, usaremos `pip` para instalar el proyecto en el entorno virtual.

Ejecute el siguiente comando en su terminal:

```none
pip install -e.
```

Esto le indica a pip que busque `pyproject.toml` en el directorio actual e instale el proyecto en modo editable o de desarrollo. El modo editable significa que cuando realice cambios en su código local, solo necesitará volver a instalar si cambia los metadatos del proyecto.

Para verificar la instalación, use el comando `pip list`:

```none
pip list
```

La salida debe mostrar el proyecto instalado y sus dependencias.
