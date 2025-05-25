# Pacotes (Packages) vs Módulos (Modules)

Para coleções maiores de código, é comum organizar módulos em um pacote.

```code
# De
pcost.py
report.py
fileparse.py

# Para
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Você escolhe um nome e cria um diretório de nível superior. `porty` no exemplo acima (claramente, escolher este nome é o primeiro passo mais importante).

Adicione um arquivo `__init__.py` ao diretório. Ele pode estar vazio.

Coloque seus arquivos fonte no diretório.
