# Divisão de Módulos para Melhor Organização do Código

À medida que seus projetos Python crescem, você pode descobrir que um único arquivo de módulo se torna bastante grande e contém vários componentes relacionados, mas distintos. Quando isso acontece, é uma boa prática dividir o módulo em um pacote com submódulos. Essa abordagem torna seu código mais organizado, mais fácil de manter e mais escalável.

## Compreendendo a Estrutura Atual

O módulo `tableformat.py` é um bom exemplo de um módulo grande. Ele contém várias classes de formatadores, cada uma responsável por formatar dados de uma maneira diferente:

- `TableFormatter` (classe base): Esta é a classe base para todas as outras classes de formatadores. Ele define a estrutura básica e os métodos que as outras classes herdarão e implementarão.
- `TextTableFormatter`: Esta classe formata dados em texto simples.
- `CSVTableFormatter`: Esta classe formata dados em formato CSV (Valores Separados por Vírgula).
- `HTMLTableFormatter`: Esta classe formata dados em formato HTML (Linguagem de Marcação de Hipertexto).

Vamos reorganizar este módulo em uma estrutura de pacote com arquivos separados para cada tipo de formatador. Isso tornará o código mais modular e mais fácil de gerenciar.

## Passo 1: Limpar Arquivos de Cache

Antes de começarmos a reorganizar o código, é uma boa ideia limpar quaisquer arquivos de cache Python. Esses arquivos são criados pelo Python para acelerar a execução do seu código, mas às vezes podem causar problemas ao fazer alterações no seu código.

```bash
cd ~/project/structly
rm -rf __pycache__
```

Nos comandos acima, `cd ~/project/structly` altera o diretório atual para o diretório `structly` em seu projeto. `rm -rf __pycache__` exclui o diretório `__pycache__` e todo o seu conteúdo. A opção `-r` significa recursivo, o que significa que ele excluirá todos os arquivos e subdiretórios dentro do diretório `__pycache__`. A opção `-f` significa forçar, o que significa que ele excluirá os arquivos sem pedir confirmação.

## Passo 2: Criar a Nova Estrutura do Pacote

Agora, vamos criar uma nova estrutura de diretórios para nosso pacote. Criaremos um diretório chamado `tableformat` e um subdiretório chamado `formats` dentro dele.

```bash
mkdir -p tableformat/formats
```

O comando `mkdir` é usado para criar diretórios. A opção `-p` significa pais, o que significa que ele criará todos os diretórios pai necessários, caso eles não existam. Portanto, se o diretório `tableformat` não existir, ele será criado primeiro e, em seguida, o diretório `formats` será criado dentro dele.

## Passo 3: Mover e Renomear o Arquivo Original

Em seguida, moveremos o arquivo original `tableformat.py` para a nova estrutura e o renomearemos para `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

O comando `mv` é usado para mover ou renomear arquivos. Neste caso, estamos movendo o arquivo `tableformat.py` para o diretório `tableformat` e renomeando-o para `formatter.py`.

## Passo 4: Dividir o Código em Arquivos Separados

Agora precisamos criar arquivos para cada formatador e mover o código relevante para eles.

### 1. Criar o arquivo do formatador base

```bash
touch tableformat/formatter.py
```

O comando `touch` é usado para criar um arquivo vazio. Neste caso, estamos criando um arquivo chamado `formatter.py` no diretório `tableformat`.

Manteremos a classe base `TableFormatter` e quaisquer funções utilitárias gerais, como `print_table` e `create_formatter`, neste arquivo. O arquivo deve ser parecido com:

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

A variável `__all__` é usada para especificar quais símbolos devem ser importados quando você usa `from module import *`. Neste caso, estamos especificando que apenas os símbolos `TableFormatter`, `print_table` e `create_formatter` devem ser importados.

A classe `TableFormatter` é a classe base para todas as outras classes de formatadores. Ele define dois métodos, `headings` e `row`, que devem ser implementados pelas subclasses.

A função `print_table` é uma função utilitária que recebe uma lista de objetos, uma lista de nomes de colunas e um objeto formatador e imprime os dados em uma tabela formatada.

A função `create_formatter` é uma função de fábrica que recebe um nome de formato como argumento e retorna um objeto formatador apropriado.

Salve e saia do arquivo após fazer essas alterações.

### 2. Criar o formatador de texto

```bash
touch tableformat/formats/text.py
```

Adicionaremos apenas a classe `TextTableFormatter` a este arquivo.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

A variável `__all__` especifica que apenas o símbolo `TextTableFormatter` deve ser importado quando você usa `from module import *`.

A instrução `from ..formatter import TableFormatter` importa a classe `TableFormatter` do arquivo `formatter.py` no diretório pai.

A classe `TextTableFormatter` herda da classe `TableFormatter` e implementa os métodos `headings` e `row` para formatar os dados em texto simples.

Salve e saia do arquivo após fazer essas alterações.

### 3. Criar o formatador CSV

```bash
touch tableformat/formats/csv.py
```

Adicionaremos apenas a classe `CSVTableFormatter` a este arquivo.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

Semelhante às etapas anteriores, estamos especificando a variável `__all__`, importando a classe `TableFormatter` e implementando os métodos `headings` e `row` para formatar os dados em formato CSV.

Salve e saia do arquivo após fazer essas alterações.

### 4. Criar o formatador HTML

```bash
touch tableformat/formats/html.py
```

Adicionaremos apenas a classe `HTMLTableFormatter` a este arquivo.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Novamente, estamos especificando a variável `__all__`, importando a classe `TableFormatter` e implementando os métodos `headings` e `row` para formatar os dados em formato HTML.

Salve e saia do arquivo após fazer essas alterações.

## Passo 5: Criar Arquivos de Inicialização do Pacote

Em Python, os arquivos `__init__.py` são usados para marcar diretórios como pacotes Python. Precisamos criar arquivos `__init__.py` nos diretórios `tableformat` e `formats`.

### 1. Criar um para o pacote `tableformat`

```bash
touch tableformat/__init__.py
```

Adicione este conteúdo ao arquivo:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Esta instrução importa todos os símbolos do arquivo `formatter.py` e os disponibiliza quando você importa o pacote `tableformat`.

Salve e saia do arquivo após fazer essas alterações.

### 2. Criar um para o pacote `formats`

```bash
touch tableformat/formats/__init__.py
```

Você pode deixar este arquivo vazio ou adicionar uma docstring simples:

```python
'''
Format implementations for different output formats.
'''
```

A docstring fornece uma breve descrição do que o pacote `formats` faz.

Salve e saia do arquivo após fazer essas alterações.

## Passo 6: Testar a Nova Estrutura

Vamos criar um teste simples para verificar se nossas alterações funcionam corretamente.

```bash
cd ~/project
touch test_tableformat.py
```

Adicione este conteúdo ao arquivo `test_tableformat.py`:

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

Este código de teste importa as funções e classes necessárias do pacote `structly`, cria formatadores de cada tipo, define alguns dados de teste e, em seguida, testa cada formatador imprimindo os dados no formato correspondente.

Salve e saia do arquivo após fazer essas alterações. Agora execute o teste:

```bash
python test_tableformat.py
```

Você deve ver os mesmos dados formatados de três maneiras diferentes (texto, CSV e HTML). Se você vir a saída esperada, significa que a reorganização do seu código foi bem-sucedida.
