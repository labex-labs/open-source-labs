# Criando um Formatador de Tabela Usando Acesso a Atributos

Em programação, o acesso a atributos é um conceito fundamental que nos permite interagir com as propriedades dos objetos. Agora, vamos colocar em prática o que aprendemos sobre acesso a atributos. Criaremos um utilitário útil: um formatador de tabela. Este formatador pegará uma coleção de objetos e os exibirá em um formato tabular, tornando os dados mais fáceis de ler e entender.

## Criando o Módulo tableformat.py

Primeiro, precisamos criar um novo arquivo Python. Este arquivo conterá o código para o nosso formatador de tabela.

Para criar o arquivo, siga estas etapas:

1. No WebIDE, clique no menu "File".
2. No menu suspenso, selecione "New File".
3. Salve o arquivo recém-criado como `tableformat.py` no diretório `/home/labex/project/`.

Agora que temos nosso arquivo, vamos escrever o código para a função `print_table()` dentro de `tableformat.py`. Esta função será responsável por formatar e imprimir nossos objetos em uma tabela.

```python
def print_table(objects, fields):
    """
    Imprime uma coleção de objetos como uma tabela formatada.

    Args:
        objects: Uma sequência de objetos
        fields: Uma lista de nomes de atributos
    """
    # Imprime o cabeçalho
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Imprime a linha separadora
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Imprime os dados
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

Vamos detalhar o que essa função faz:

1. Ela recebe dois argumentos: uma sequência de objetos e uma lista de nomes de atributos. A sequência de objetos são os dados que queremos exibir, e a lista de nomes de atributos informa à função quais propriedades dos objetos mostrar.
2. Ela imprime uma linha de cabeçalho. A linha de cabeçalho contém os nomes dos atributos nos quais estamos interessados.
3. Ela imprime uma linha separadora. Essa linha ajuda a separar visualmente o cabeçalho dos dados.
4. Para cada objeto na sequência, ela imprime o valor de cada atributo especificado. Ela usa a função `getattr()` para acessar o valor do atributo de cada objeto.

Agora, vamos testar nossa função `print_table()` para ver se ela funciona como esperado.

```python
# Abra um shell interativo do Python
python3

# Importe nossos módulos
from stock import read_portfolio
import tableformat

# Leia os dados da carteira
portfolio = read_portfolio('portfolio.csv')

# Imprima a carteira como uma tabela com colunas de nome, ações e preço
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Quando você executar o código acima, deverá ver a seguinte saída:

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Uma das grandes vantagens da nossa função `print_table()` é sua flexibilidade. Podemos alterar as colunas que são exibidas simplesmente alterando a lista `fields`.

```python
# Mostre apenas ações e nome
tableformat.print_table(portfolio, ['shares', 'name'])
```

A execução deste código fornecerá a seguinte saída:

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

O poder dessa abordagem reside em sua generalidade. Podemos usar a mesma função `print_table()` para imprimir tabelas para qualquer tipo de objeto, desde que saibamos os nomes dos atributos que queremos exibir. Isso torna nosso formatador de tabela uma ferramenta muito útil em nosso kit de ferramentas de programação.
