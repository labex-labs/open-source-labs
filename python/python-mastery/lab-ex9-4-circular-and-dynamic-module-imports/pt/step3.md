# Implementando o Registro de Subclasses

Em programação, as importações circulares podem ser um problema complicado. Em vez de importar diretamente as classes de formatador, podemos usar um padrão de registro. Nesse padrão, as subclasses se registram com sua classe pai. Esta é uma maneira comum e eficaz de evitar importações circulares.

Primeiro, vamos entender como podemos descobrir o nome do módulo de uma classe. O nome do módulo é importante porque o usaremos em nosso padrão de registro. Para fazer isso, executaremos um comando Python no terminal.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

Quando você executa este comando, verá uma saída como esta:

```
structly.tableformat.formats.text
text
```

Esta saída mostra que podemos extrair o nome do módulo da própria classe. Usaremos este nome de módulo mais tarde para registrar as subclasses.

Agora, vamos modificar a classe `TableFormatter` no arquivo `tableformat/formatter.py` para adicionar um mecanismo de registro. Abra este arquivo no WebIDE. Adicionaremos algum código à classe `TableFormatter`. Este código nos ajudará a registrar as subclasses automaticamente.

```python
class TableFormatter(ABC):
    _formats = { }  # Dicionário para armazenar formatadores registrados

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

O método `__init_subclass__` é um método especial em Python. Ele é chamado sempre que uma subclasse de `TableFormatter` é criada. Neste método, extraímos o nome do módulo da subclasse e o usamos como uma chave para registrar a subclasse no dicionário `_formats`.

Em seguida, precisamos modificar a função `create_formatter` para usar o dicionário de registro. Esta função é responsável por criar o formatador apropriado com base no nome fornecido.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Depois de fazer essas alterações, salve o arquivo. Em seguida, vamos testar se o programa ainda funciona. Executaremos o script `stock.py`.

```bash
python3 stock.py
```

Se o programa for executado corretamente, significa que nossas alterações não quebraram nada. Agora, vamos dar uma olhada no conteúdo do dicionário `_formats` para ver como o registro funciona.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

Você deve ver uma saída como esta:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

Esta saída confirma que nossas subclasses estão sendo registradas corretamente no dicionário `_formats`. No entanto, ainda temos algumas importações no meio do arquivo. Na próxima etapa, corrigiremos esse problema usando importações dinâmicas.
