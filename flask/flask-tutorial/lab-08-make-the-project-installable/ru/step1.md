# Описание проекта

Во - первых, нам нужно создать файл `pyproject.toml`, чтобы описать наш проект и способ его сборки.

Файл `pyproject.toml` должен выглядеть так:

```toml
# pyproject.toml

[project]
name = "flaskr" # имя проекта
version = "1.0.0" # версия проекта
dependencies = [
    "flask", # зависимости проекта
]

[build - system]
requires = ["setuptools"] # требуемая сборочная система
build - backend = "setuptools.build_meta" # бэкенд сборочной системы
```
