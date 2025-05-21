# Criando uma Classe Base e Modificando a Função de Impressão

Em programação, herança é um conceito poderoso que nos permite criar uma hierarquia de classes. Para começar a usar herança para gerar dados em diferentes formatos, primeiro precisamos criar uma classe base. Uma classe base serve como um modelo para outras classes, definindo um conjunto comum de métodos que suas subclasses podem herdar e substituir.

Agora, vamos criar uma classe base que definirá a interface para todos os formatadores de tabela. Abra o arquivo `tableformat.py` no WebIDE e adicione o seguinte código no topo do arquivo:

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

A classe `TableFormatter` é uma classe base abstrata. Uma classe base abstrata é uma classe que define métodos, mas não fornece implementações para eles. Em vez disso, ela espera que suas subclasses forneçam essas implementações. As exceções `NotImplementedError` são usadas para indicar que esses métodos devem ser substituídos pelas subclasses. Se uma subclasse não substituir esses métodos e tentarmos usá-los, um erro será gerado.

Em seguida, precisamos modificar a função `print_table()` para usar a classe `TableFormatter`. A função `print_table()` é usada para imprimir uma tabela de dados de uma lista de objetos. Ao modificá-la para usar a classe `TableFormatter`, podemos tornar a função mais flexível e capaz de trabalhar com diferentes formatos de tabela.

Substitua a função `print_table()` existente pelo seguinte código:

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

A principal mudança aqui é que `print_table()` agora recebe um parâmetro `formatter`, que deve ser uma instância de `TableFormatter` ou uma subclasse. Isso significa que podemos passar diferentes formatadores de tabela para a função `print_table()`, e ela usará o formatador apropriado para imprimir a tabela. A função delega a responsabilidade de formatação ao objeto formatador, chamando seus métodos `headings()` e `row()`.

Vamos testar nossas alterações tentando usar a classe base `TableFormatter`:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Quando você executar este código, você deve ver um erro:

```
Traceback (most recent call last):
...
NotImplementedError
```

Este erro ocorre porque estamos tentando usar a classe base abstrata diretamente, mas ela não fornece implementações para seus métodos. Como os métodos `headings()` e `row()` na classe `TableFormatter` lançam `NotImplementedError`, o Python não sabe o que fazer quando esses métodos são chamados. Na próxima etapa, criaremos uma subclasse concreta que fornece essas implementações.
