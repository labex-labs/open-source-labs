# Construindo a Aplicação

Primeiramente, precisamos criar um arquivo wheel para nossa aplicação. Usaremos a ferramenta `build` para isso. Instale a ferramenta `build` usando pip, caso ainda não a tenha:

```bash
# Install the build tool
pip install build
```

Agora, use a ferramenta `build` para criar o arquivo wheel:

```bash
# Build the wheel file
python -m build --wheel
```

O arquivo wheel deve estar no diretório `dist` com um nome como `flaskr-1.0.0-py3-none-any.whl`.
