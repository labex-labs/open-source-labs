# Compreendendo o Problema de Importação

Vamos começar entendendo o que são as importações de módulos. Em Python, quando você deseja usar funções, classes ou variáveis de outro arquivo (módulo), você usa a instrução `import`. No entanto, a forma como você estrutura suas importações pode levar a vários problemas.

Agora, vamos examinar um exemplo de uma estrutura de módulo problemática. O código em `tableformat/formatter.py` tem importações espalhadas por todo o arquivo. Isso pode não parecer um grande problema a princípio, mas cria problemas de manutenção e dependência.

Primeiro, abra o explorador de arquivos do WebIDE e navegue até o diretório `structly`. Executaremos alguns comandos para entender a estrutura atual do projeto. O comando `cd` é usado para alterar o diretório de trabalho atual, e o comando `ls -la` lista todos os arquivos e diretórios no diretório atual, incluindo os ocultos.

```bash
cd ~/project/structly
ls -la
```

Isso mostrará os arquivos no diretório do projeto. Agora, vamos olhar para um dos arquivos problemáticos usando o comando `cat`, que exibe o conteúdo de um arquivo.

```bash
cat tableformat/formatter.py
```

Você deve ver um código semelhante ao seguinte:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Observe a colocação das instruções de importação no meio do arquivo. Isso é problemático por várias razões:

1.  Torna o código mais difícil de ler e manter. Quando você está olhando para um arquivo, espera ver todas as importações no início para que possa entender rapidamente de quais módulos externos o arquivo depende.
2.  Pode levar a problemas de importação circular. As importações circulares acontecem quando dois ou mais módulos dependem um do outro, o que pode causar erros e fazer com que seu código se comporte de forma inesperada.
3.  Quebra a convenção Python de colocar todas as importações no topo de um arquivo. Seguir as convenções torna seu código mais legível e mais fácil de entender para outros desenvolvedores.

Nos passos seguintes, exploraremos esses problemas com mais detalhes e aprenderemos como resolvê-los.
