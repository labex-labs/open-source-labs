# Instalar o Projeto

Em seguida, usaremos `pip` para instalar o projeto no ambiente virtual.

Execute o seguinte comando no seu terminal:

```none
pip install -e .
```

Isso informa ao pip para encontrar `pyproject.toml` no diretório atual e instalar o projeto no modo editável ou de desenvolvimento. O modo editável significa que, à medida que você faz alterações no seu código local, você só precisará reinstalar se alterar os metadados do projeto.

Para verificar a instalação, use o comando `pip list`:

```none
pip list
```

A saída deve mostrar o projeto instalado e suas dependências.
