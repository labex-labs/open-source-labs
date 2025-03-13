# Понимание проблемы импорта

Начнем с понимания, что такое импорт модулей. В Python, когда вы хотите использовать функции, классы или переменные из другого файла (модуля), вы используете оператор `import`. Однако способ организации импортов может привести к различным проблемам.

Теперь мы рассмотрим пример проблемной структуры модулей. В коде файла `tableformat/formatter.py` импорты разбросаны по всему файлу. На первый взгляд это может показаться несущественным, но это создает проблемы с поддержкой и зависимостями.

Сначала откройте проводник файлов в WebIDE и перейдите в директорию `structly`. Мы выполним несколько команд, чтобы понять текущую структуру проекта. Команда `cd` используется для изменения текущей рабочей директории, а команда `ls -la` выводит список всех файлов и директорий в текущей директории, включая скрытые.

```bash
cd ~/project/structly
ls -la
```

Это покажет вам файлы в директории проекта. Теперь мы посмотрим на один из проблемных файлов с помощью команды `cat`, которая отображает содержимое файла.

```bash
cat tableformat/formatter.py
```

Вы должны увидеть код, похожий на следующий:

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

Обратите внимание на то, что операторы импорта расположены в середине файла. Это проблематично по нескольким причинам:

1. Это делает код труднее читать и поддерживать. Когда вы просматриваете файл, вы ожидаете увидеть все импорты в начале, чтобы быстро понять, от каких внешних модулей зависит файл.
2. Это может привести к проблемам с циклическими импортами. Циклические импорты возникают, когда два или более модулей зависят друг от друга, что может вызвать ошибки и сделать поведение вашего кода непредсказуемым.
3. Это нарушает соглашение Python о размещении всех импортов в верхней части файла. Следование соглашениям делает ваш код более читаемым и легче для понимания другими разработчиками.

В следующих шагах мы более подробно рассмотрим эти проблемы и научимся их решать.
