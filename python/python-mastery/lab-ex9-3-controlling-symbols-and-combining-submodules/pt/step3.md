# Exportando Tudo do Pacote

Em Python, a organização de pacotes é crucial para gerenciar o código de forma eficaz. Agora, vamos levar a organização do nosso pacote um passo adiante. Definiremos quais símbolos devem ser exportados no nível do pacote. Exportar símbolos significa disponibilizar certas funções, classes ou variáveis para outras partes do seu código ou para outros desenvolvedores que possam usar seu pacote.

## Adicionando `__all__` ao Pacote

Ao trabalhar com pacotes Python, você pode querer controlar quais símbolos são acessíveis quando alguém usa a instrução `from structly import *`. É aqui que a lista `__all__` é útil. Ao adicionar uma lista `__all__` ao arquivo `__init__.py` do pacote, você pode controlar precisamente quais símbolos estão disponíveis quando alguém usa a instrução `from structly import *`.

Primeiro, vamos criar ou atualizar o arquivo `__init__.py`. Usaremos o comando `touch` para criar o arquivo, caso ele não exista.

```bash
touch ~/project/structly/__init__.py
```

Agora, abra o arquivo `__init__.py` e adicione uma lista `__all__`. Esta lista deve incluir todos os símbolos que queremos exportar. Os símbolos são agrupados com base em sua origem, como os módulos `structure`, `reader` e `tableformat`.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

Após adicionar o código, salve o arquivo e saia do editor.

## Compreendendo `import *`

O padrão `from module import *` geralmente não é recomendado na maioria dos códigos Python. Existem várias razões para isso:

1. Pode poluir seu namespace com símbolos inesperados. Isso significa que você pode acabar com variáveis ou funções em seu namespace atual que você não esperava, o que pode levar a conflitos de nomes.
2. Torna obscuro de onde vêm os símbolos específicos. Quando você usa `import *`, é difícil dizer de qual módulo um símbolo está vindo, o que pode tornar seu código mais difícil de entender e manter.
3. Pode levar a problemas de sombreamento (shadowing). O sombreamento ocorre quando uma variável ou função local tem o mesmo nome que uma variável ou função de outro módulo, o que pode causar um comportamento inesperado.

No entanto, existem casos específicos em que o uso de `import *` é apropriado:

- Para pacotes projetados para serem usados como um todo coeso. Se um pacote for destinado a ser usado como uma única unidade, o uso de `import *` pode facilitar o acesso a todos os símbolos necessários.
- Quando um pacote define uma interface clara via `__all__`. Ao usar a lista `__all__`, você pode controlar quais símbolos são exportados, tornando mais seguro o uso de `import *`.
- Para uso interativo, como em um REPL (Read-Eval-Print Loop) Python. Em um ambiente interativo, pode ser conveniente importar todos os símbolos de uma vez.

## Testando com Import \*

Para verificar se podemos importar todos os símbolos de uma vez, vamos criar outro arquivo de teste. Usaremos o comando `touch` para criar o arquivo.

```bash
touch ~/project/test_import_all.py
```

Agora, abra o arquivo `test_import_all.py` e adicione o seguinte conteúdo. Este código importa todos os símbolos do pacote `structly` e, em seguida, testa se alguns dos símbolos importantes estão disponíveis.

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

Salve o arquivo e saia do editor. Agora, vamos executar o teste. Primeiro, navegue até o diretório do projeto usando o comando `cd` e, em seguida, execute o script Python.

```bash
cd ~/project
python test_import_all.py
```

Se tudo estiver configurado corretamente, você deverá ver a confirmação de que todos os símbolos foram importados com sucesso.
