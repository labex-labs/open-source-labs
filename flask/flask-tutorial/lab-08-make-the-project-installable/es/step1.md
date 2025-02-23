# Describir el proyecto

Primero, necesitamos crear un archivo `pyproject.toml` para describir nuestro proyecto y cómo construirlo.

El archivo `pyproject.toml` debería verse así:

```toml
# pyproject.toml

[project]
name = "flaskr" # nombre del proyecto
version = "1.0.0" # versión del proyecto
dependencies = [
    "flask", # dependencias del proyecto
]

[build-system]
requires = ["setuptools"] # sistema de compilación requerido
build-backend = "setuptools.build_meta" # sistema de compilación de backend
```
