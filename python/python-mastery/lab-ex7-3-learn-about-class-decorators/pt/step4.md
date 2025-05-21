# Adicionando Funcionalidade de Conversão de Linha

Em programação, é frequentemente útil criar instâncias de uma classe a partir de linhas de dados, especialmente ao lidar com dados de fontes como arquivos CSV. Nesta seção, adicionaremos a capacidade de criar instâncias da classe `Structure` a partir de linhas de dados. Faremos isso implementando um método de classe `from_row` na classe `Structure`.

1. Primeiro, você precisa abrir o arquivo `structure.py`. É aqui que faremos as alterações no nosso código. Use o seguinte comando no seu terminal:

```bash
code ~/project/structure.py
```

2. Em seguida, modificaremos a função `validate_attributes`. Esta função é um decorador de classe que extrai instâncias de `Validator` e constrói as listas `_fields` e `_types` automaticamente. Vamos atualizá-la para também coletar informações de tipo.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Nesta função atualizada, estamos coletando o atributo `expected_type` de cada validador e armazenando-o na variável de classe `_types`. Isso será útil mais tarde, quando convertermos dados de linhas para os tipos corretos.

3. Agora, adicionaremos o método de classe `from_row` à classe `Structure`. Este método nos permitirá criar uma instância da classe a partir de uma linha de dados, que pode ser uma lista ou uma tupla.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

Veja como este método funciona:

- Ele recebe uma linha de dados, que pode estar na forma de uma lista ou uma tupla.
- Ele converte cada valor na linha para o tipo esperado usando a função correspondente da lista `_types`.
- Em seguida, ele cria e retorna uma nova instância da classe usando os valores convertidos.

4. Depois de fazer essas alterações, salve o arquivo `structure.py`. Isso garante que as alterações no seu código sejam preservadas.

5. Vamos testar nosso método `from_row` para garantir que ele funcione como esperado. Criaremos um teste simples usando a classe `Stock`. Execute o seguinte comando no seu terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Você deverá ver uma saída semelhante a esta:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Observe que os valores de string '100' e '490.1' foram convertidos automaticamente para os tipos corretos (inteiro e float). Isso mostra que nosso método `from_row` está funcionando corretamente.

6. Finalmente, vamos tentar ler dados de um arquivo CSV usando nosso módulo `reader.py`. Execute o seguinte comando no seu terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Você deverá ver a saída mostrando as ações do arquivo CSV:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

O método `from_row` nos permite converter facilmente dados CSV em instâncias da classe `Stock`. Quando combinado com a função `read_csv_as_instances`, temos uma maneira poderosa de carregar e trabalhar com dados estruturados.
