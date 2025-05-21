# Explorando as Importações Circulares

Uma importação circular é uma situação em que dois ou mais módulos dependem um do outro. Especificamente, quando o módulo A importa o módulo B, e o módulo B também importa o módulo A, direta ou indiretamente. Isso cria um ciclo de dependência que o sistema de importação do Python não consegue resolver corretamente. Em termos mais simples, o Python fica preso em um loop tentando descobrir qual módulo importar primeiro, e isso pode levar a erros em seu programa.

Vamos experimentar com nosso código para ver como as importações circulares podem causar problemas.

Primeiro, executaremos o programa de estoque para verificar se ele funciona com a estrutura atual. Esta etapa nos ajuda a estabelecer uma linha de base e ver o programa funcionando como esperado antes de fazermos quaisquer alterações.

```bash
cd ~/project/structly
python3 stock.py
```

O programa deve ser executado corretamente e exibir os dados de estoque em uma tabela formatada. Se isso acontecer, significa que a estrutura de código atual está funcionando bem, sem problemas de importação circular.

Agora, vamos modificar o arquivo `formatter.py`. Normalmente, é uma boa prática mover as importações para o topo de um arquivo. Isso torna o código mais organizado e mais fácil de entender rapidamente.

```bash
cd ~/project/structly
```

Abra `tableformat/formatter.py` no WebIDE. Moveremos as seguintes importações para o topo do arquivo, logo após as importações existentes. Essas importações são para diferentes formatadores de tabela, como texto, CSV e HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Então, o início do arquivo agora deve ser assim:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Salve o arquivo e tente executar o programa de estoque novamente.

```bash
python3 stock.py
```

Você deve ver uma mensagem de erro sobre `TableFormatter` não estar definido. Este é um sinal claro de um problema de importação circular.

O problema ocorre por causa da seguinte cadeia de eventos:

1.  `formatter.py` tenta importar `TextTableFormatter` de `formats/text.py`.
2.  `formats/text.py` importa `TableFormatter` de `formatter.py`.
3.  Quando o Python tenta resolver essas importações, ele fica preso em um loop porque não consegue decidir qual módulo importar totalmente primeiro.

Vamos reverter nossas alterações para fazer o programa funcionar novamente. Edite `tableformat/formatter.py` e mova as importações de volta para onde estavam originalmente (após a definição da classe `TableFormatter`).

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
```

Execute o programa novamente para confirmar que está funcionando.

```bash
python3 stock.py
```

Isso demonstra que, embora ter importações no meio do arquivo não seja a melhor prática em termos de organização do código, isso foi feito para evitar um problema de importação circular. Nos próximos passos, exploraremos soluções melhores.
