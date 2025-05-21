# Criando uma API Amigável para Mixins

Mixins são poderosos, mas usar herança múltipla diretamente pode parecer complexo. Nesta etapa, melhoraremos a função `create_formatter()` para ocultar essa complexidade, fornecendo uma API mais fácil para os usuários.

Primeiro, certifique-se de que `tableformat.py` esteja aberto no seu editor:

```bash
cd ~/project
touch tableformat.py
```

Encontre a função `create_formatter()` existente:

```python
# Função existente em tableformat.py
def create_formatter(name):
    """
    Cria um formatador apropriado com base no nome.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Substitua a _definição inteira existente_ da função `create_formatter()` pela versão aprimorada abaixo. Esta nova versão aceita argumentos opcionais para formatos de coluna e cabeçalhos em maiúsculas.

```python
# Substitua o antigo create_formatter por este em tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Cria um formatador com aprimoramentos opcionais.

    Parâmetros:
    name : str
        Nome do formatador ('text', 'csv', 'html')
    column_formats : list, optional
        Lista de strings de formato para formatação de coluna.
        Observação: Depende da existência de ColumnFormatMixin acima desta função.
    upper_headers : bool, optional
        Se deve converter os cabeçalhos para maiúsculas.
        Observação: Depende da existência de UpperHeadersMixin acima desta função.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Constrói a lista de herança dinamicamente
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # A classe base do formatador vem por último

    # Cria a classe personalizada dinamicamente
    # Precisa garantir que ColumnFormatMixin e UpperHeadersMixin sejam definidos antes deste ponto
    class CustomFormatter(*bases):
        # Define os formatos se ColumnFormatMixin for usado
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Retorna uma instância da classe criada dinamicamente
```

_Autocorreção: Crie dinamicamente a tupla de classe para herança em vez de várias ramificações if/elif._

Esta função aprimorada primeiro determina a classe base do formatador (`TextTableFormatter`, `CSVTableFormatter`, etc.). Em seguida, com base nos argumentos opcionais `column_formats` e `upper_headers`, ela constrói dinamicamente uma nova classe (`CustomFormatter`) que herda dos mixins necessários e da classe base do formatador. Finalmente, ela retorna uma instância deste formatador personalizado.

**Lembre-se de salvar as alterações em `tableformat.py`.**

Agora, vamos testar nossa função aprimorada. **Certifique-se de ter salvo a função `create_formatter` atualizada em `tableformat.py`.**

Primeiro, teste a formatação de coluna. Crie `step3_test1.py`:

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Usando os mesmos formatos de antes, sujeito a problemas de tipo.
# Use formatos compatíveis com strings se '%d', '%.2f' causarem erros.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Execute o script:

```bash
python3 step3_test1.py
```

Você deve ver a tabela com colunas formatadas (novamente, sujeito ao tratamento de tipo do formato de preço):

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

Em seguida, teste os cabeçalhos em maiúsculas. Crie `step3_test2.py`:

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Execute o script:

```bash
python3 step3_test2.py
```

Você deve ver a tabela com cabeçalhos em maiúsculas:

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Finalmente, combine ambas as opções. Crie `step3_test3.py`:

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Usando os mesmos formatos de antes
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Execute o script:

```bash
python3 step3_test3.py
```

Isso deve exibir uma tabela com colunas formatadas e cabeçalhos em maiúsculas:

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
------------------------------------------------------------------
```

A função aprimorada também funciona com outros tipos de formatador. Por exemplo, experimente com o formatador CSV. Crie `step3_test4.py`:

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# Para CSV, certifique-se de que os formatos produzam campos CSV válidos.
# Adicionando aspas ao redor do campo de nome da string.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Execute o script:

```bash
python3 step3_test4.py
```

Isso deve produzir cabeçalhos em maiúsculas e colunas formatadas em formato CSV (novamente, possível problema de tipo para formatação `%d`/`%.2f` em strings passadas de `print_table`):

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

Ao aprimorar a função `create_formatter()`, criamos uma API amigável para o usuário. Os usuários agora podem aplicar facilmente as funcionalidades mixin sem precisar gerenciar a estrutura de herança múltipla por conta própria.
