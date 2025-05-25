# Exercício 9.1: Criando um pacote simples

Crie um diretório chamado `porty/` e coloque todos os arquivos Python acima nele. Adicionalmente, crie um arquivo `__init__.py` vazio e coloque-o no diretório. Você deve ter um diretório de arquivos como este:

    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py

Remova o arquivo `__pycache__` que está no seu diretório. Ele contém módulos Python pré-compilados de antes. Queremos começar do zero.

Tente importar alguns dos módulos do pacote:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

Se essas importações falharem, vá para o arquivo apropriado e corrija as importações do módulo para incluir uma importação relativa ao pacote. Por exemplo, uma instrução como `import fileparse` pode mudar para o seguinte:

    # report.py
    from . import fileparse
    ...

Se você tiver uma instrução como `from fileparse import parse_csv`, altere o código para o seguinte:

    # report.py
    from .fileparse import parse_csv
    ...
