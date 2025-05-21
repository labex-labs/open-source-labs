# Compreendendo o Problema com a Formatação de Colunas

Nesta etapa, vamos analisar uma limitação na nossa implementação atual de formatação de tabelas. Também examinaremos algumas soluções possíveis para este problema.

Primeiro, vamos entender o que faremos. Abriremos o editor VSCode e analisaremos o arquivo `tableformat.py` no diretório do projeto. Este arquivo é importante porque contém o código que nos permite formatar dados tabulares de diferentes maneiras, como em formatos de texto, CSV ou HTML.

Para abrir o arquivo, usaremos os seguintes comandos no terminal. O comando `cd` altera o diretório para o diretório do projeto, e o comando `code` abre o arquivo `tableformat.py` no VSCode.

```bash
cd ~/project
touch tableformat.py
```

Ao abrir o arquivo, você notará que há várias classes definidas. Essas classes desempenham diferentes papéis na formatação dos dados da tabela.

- `TableFormatter`: Esta é uma classe base abstrata. Ela possui métodos que são usados para formatar os títulos e linhas da tabela. Pense nela como um modelo para outras classes de formatação.
- `TextTableFormatter`: Esta classe é usada para gerar a tabela em formato de texto simples.
- `CSVTableFormatter`: É responsável por formatar os dados da tabela em formato CSV (Valores Separados por Vírgula).
- `HTMLTableFormatter`: Esta classe formata os dados da tabela em formato HTML.

Há também uma função `print_table()` no arquivo. Esta função usa as classes de formatação que acabamos de mencionar para exibir os dados tabulares.

Agora, vamos ver como essas classes funcionam. No seu diretório `/home/labex/project`, crie um novo arquivo chamado `step1_test1.py` usando seu editor ou o comando `touch`. Adicione o seguinte código Python a ele:

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Salve o arquivo e execute-o a partir do seu terminal:

```bash
python3 step1_test1.py
```

Após executar o script, você deverá ver uma saída semelhante a esta:

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Agora, vamos encontrar o problema. Observe que os valores na coluna `price` não estão formatados de forma consistente. Alguns valores têm uma casa decimal, como 32.2, enquanto outros têm duas casas decimais, como 51.23. Em dados financeiros, geralmente queremos que a formatação seja consistente.

Veja como queremos que a saída se pareça:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Uma maneira de corrigir isso é modificar a função `print_table()` para aceitar especificações de formato. Vamos ver como isso funciona _sem_ realmente modificar `tableformat.py`. Crie um novo arquivo chamado `step1_test2.py` com o seguinte conteúdo. Este script redefine a função `print_table` localmente para fins de demonstração.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Execute este script:

```bash
python3 step1_test2.py
```

Esta abordagem demonstra a passagem de formatos, mas modificar `print_table` tem uma desvantagem: alterar a interface da função pode quebrar o código existente que usa a versão original.

Outra abordagem é criar um formatador personalizado por meio de subclassing. Podemos criar uma nova classe que herda de `TextTableFormatter` e substituir o método `row()`. Crie um arquivo `step1_test3.py`:

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Execute o script:

```bash
python3 step1_test3.py
```

Esta solução funciona para demonstrar o subclassing, mas criar uma nova classe para cada variação de formatação não é conveniente. Além disso, você está vinculado à classe base da qual herda (aqui, `TextTableFormatter`).

Na próxima etapa, exploraremos uma solução mais elegante usando classes mixin.
