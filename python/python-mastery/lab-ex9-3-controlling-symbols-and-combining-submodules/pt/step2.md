# Controlando Símbolos Exportados com `__all__`

Em Python, quando você usa a instrução `from module import *`, pode querer controlar quais símbolos (funções, classes, variáveis) são importados de um módulo. É aqui que a variável `__all__` é útil. A instrução `from module import *` é uma maneira de importar todos os símbolos de um módulo para o namespace atual. No entanto, às vezes você não quer importar todos os símbolos, especialmente se houver muitos ou se alguns forem destinados a serem internos ao módulo. A variável `__all__` permite que você especifique exatamente quais símbolos devem ser importados ao usar esta instrução.

## O que é `__all__`?

A variável `__all__` é uma lista de strings. Cada string nesta lista representa um símbolo (função, classe ou variável) que um módulo exporta quando alguém usa a instrução `from module import *`. Se a variável `__all__` não estiver definida em um módulo, a instrução `import *` importará todos os símbolos que não começam com um sublinhado. Símbolos que começam com um sublinhado são tipicamente considerados privados ou internos ao módulo e não devem ser importados diretamente.

## Modificando Cada Submódulo

Agora, vamos adicionar a variável `__all__` a cada submódulo no pacote `structly`. Isso nos ajudará a controlar quais símbolos são exportados de cada submódulo quando alguém usa a instrução `from module import *`.

1. Primeiro, vamos modificar `structure.py`:

```bash
touch ~/project/structly/structure.py
```

Este comando cria um novo arquivo chamado `structure.py` no diretório `structly` do seu projeto. Após criar o arquivo, precisamos adicionar a variável `__all__`. Adicione esta linha perto do topo do arquivo, logo após as instruções de importação:

```python
__all__ = ['Structure']
```

Esta linha diz ao Python que, quando alguém usa `from structure import *`, apenas o símbolo `Structure` será importado. Salve o arquivo e saia do editor.

2. Em seguida, vamos modificar `reader.py`:

```bash
touch ~/project/structly/reader.py
```

Este comando cria um novo arquivo chamado `reader.py` no diretório `structly`. Agora, procure no arquivo todas as funções que começam com `read_csv_as_`. Essas funções são as que queremos exportar. Em seguida, adicione uma lista `__all__` com todos esses nomes de funções. Deve ser algo parecido com isto:

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

Observe que os nomes reais das funções podem variar dependendo do que você encontrar no arquivo. Certifique-se de incluir todas as funções `read_csv_as_*` que você encontrar. Salve o arquivo e saia do editor.

3. Agora, vamos modificar `tableformat.py`:

```bash
touch ~/project/structly/tableformat.py
```

Este comando cria um novo arquivo chamado `tableformat.py` no diretório `structly`. Adicione esta linha perto do topo do arquivo:

```python
__all__ = ['create_formatter', 'print_table']
```

Esta linha especifica que, quando alguém usa `from tableformat import *`, apenas os símbolos `create_formatter` e `print_table` serão importados. Salve o arquivo e saia do editor.

## Importações Unificadas em `__init__.py`

Agora que cada módulo define o que exporta, podemos atualizar o arquivo `__init__.py` para importar todos esses símbolos. O arquivo `__init__.py` é um arquivo especial em pacotes Python. Ele é executado quando o pacote é importado e pode ser usado para inicializar o pacote e importar símbolos de submódulos.

```bash
touch ~/project/structly/__init__.py
```

Este comando cria um novo arquivo `__init__.py` no diretório `structly`. Mude o conteúdo do arquivo para:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Essas linhas importam todos os símbolos exportados dos submódulos `structure`, `reader` e `tableformat`. O ponto (`.`) antes dos nomes dos módulos indica que estas são importações relativas, o que significa que são importações de dentro do mesmo pacote. Salve o arquivo e saia do editor.

## Testando Nossas Mudanças

Vamos criar um arquivo de teste simples para verificar se nossas alterações funcionam. Este arquivo de teste tentará importar os símbolos que especificamos nas variáveis `__all__` e imprimirá uma mensagem de sucesso se as importações forem bem-sucedidas.

```bash
touch ~/project/test_structly.py
```

Este comando cria um novo arquivo chamado `test_structly.py` no diretório do projeto. Adicione este conteúdo ao arquivo:

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

Essas linhas tentam importar a classe `Structure`, a função `read_csv_as_instances` e as funções `create_formatter` e `print_table` do pacote `structly`. Se as importações forem bem-sucedidas, o programa imprimirá a mensagem "Successfully imported all required symbols!". Salve o arquivo e saia do editor. Agora vamos executar este teste:

```bash
cd ~/project
python test_structly.py
```

O comando `cd ~/project` altera o diretório de trabalho atual para o diretório do projeto. O comando `python test_structly.py` executa o script `test_structly.py`. Se tudo estiver funcionando corretamente, você deverá ver a mensagem "Successfully imported all required symbols!" impressa na tela.
