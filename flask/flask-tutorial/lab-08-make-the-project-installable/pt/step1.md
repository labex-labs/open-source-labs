# Descrever o Projeto

Primeiro, precisamos criar um arquivo `pyproject.toml` para descrever nosso projeto e como construí-lo.

O arquivo `pyproject.toml` deve ser semelhante a este:

```toml
# pyproject.toml

[project]
name = "flaskr" # nome do projeto
version = "1.0.0" # versão do projeto
dependencies = [
    "flask", # dependências do projeto
]

[build-system]
requires = ["setuptools"] # sistema de build requerido
build-backend = "setuptools.build_meta" # backend do sistema de build
```
