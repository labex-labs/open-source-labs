# Usando Importações Dinâmicas

Em programação, as importações são usadas para trazer código de outros módulos para que possamos usar sua funcionalidade. No entanto, às vezes, ter importações no meio de um arquivo pode tornar o código um pouco confuso e difícil de entender. Nesta parte, aprenderemos como usar importações dinâmicas para resolver esse problema. As importações dinâmicas são um recurso poderoso que nos permite carregar módulos em tempo de execução, o que significa que só carregamos um módulo quando realmente precisamos dele.

Primeiro, precisamos remover as instruções de importação que estão atualmente colocadas após a classe `TableFormatter`. Essas importações são importações estáticas, que são carregadas quando o programa é iniciado. Para fazer isso, abra o arquivo `tableformat/formatter.py` no WebIDE. Depois de abrir o arquivo, encontre e exclua as seguintes linhas:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Se você tentar executar o programa agora, executando o seguinte comando no terminal:

```bash
python3 stock.py
```

O programa falhará. A razão é que os formatadores não serão registrados no dicionário `_formats`. Você verá uma mensagem de erro sobre um formato desconhecido. Isso ocorre porque o programa não consegue encontrar as classes de formatador de que precisa para funcionar corretamente.

Para corrigir esse problema, modificaremos a função `create_formatter`. O objetivo é importar dinamicamente o módulo necessário quando ele for necessário. Atualize a função conforme mostrado abaixo:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

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

A linha mais importante nesta função é:

```python
__import__(f'{__package__}.formats.{name}')
```

Esta linha importa dinamicamente o módulo com base no nome do formato. Quando o módulo é importado, sua subclasse de `TableFormatter` se registra automaticamente. Isso é graças ao método `__init_subclass__` que adicionamos anteriormente. Este método é um método especial do Python que é chamado quando uma subclasse é criada e, em nosso caso, é usado para registrar a classe do formatador.

Depois de fazer essas alterações, salve o arquivo. Em seguida, execute o programa novamente usando o seguinte comando:

```bash
python3 stock.py
```

O programa agora deve funcionar corretamente, mesmo que tenhamos removido as importações estáticas. Para verificar se a importação dinâmica está funcionando conforme o esperado, limparemos o dicionário `_formats` e, em seguida, chamaremos a função `create_formatter`. Execute o seguinte comando no terminal:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

Você deve ver uma saída semelhante a esta:

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

Esta saída confirma que a importação dinâmica está carregando o módulo e registrando a classe do formatador quando necessário.

Ao usar importações dinâmicas e registro de classe, criamos uma estrutura de código mais limpa e fácil de manter. Aqui estão os benefícios:

1.  Todas as importações agora estão no topo do arquivo, o que segue as convenções do Python. Isso torna o código mais fácil de ler e entender.
2.  Eliminamos as importações circulares. As importações circulares podem causar problemas em um programa, como loops infinitos ou erros difíceis de depurar.
3.  O código é mais flexível. Agora, podemos adicionar novos formatadores sem modificar a função `create_formatter`. Isso é muito útil em um cenário do mundo real, onde novos recursos podem ser adicionados ao longo do tempo.

Este padrão de uso de importações dinâmicas e registro de classe é comumente usado em sistemas de plug-in e frameworks. Nesses sistemas, os componentes precisam ser carregados dinamicamente com base nas necessidades do usuário ou nos requisitos do programa.
