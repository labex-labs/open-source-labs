# Исследование циклических импортов

Циклический импорт - это ситуация, когда два или более модулей зависят друг от друга. Конкретно, когда модуль A импортирует модуль B, а модуль B также импортирует модуль A, напрямую или косвенно. Это создает цикл зависимостей, который система импорта Python не может правильно разрешить. Проще говоря, Python попадает в цикл, пытаясь понять, какой модуль импортировать первым, и это может привести к ошибкам в вашей программе.

Попробуем провести эксперимент с нашим кодом, чтобы увидеть, как циклические импорты могут вызвать проблемы.

Сначала мы запустим программу для работы с акциями, чтобы проверить, работает ли она с текущей структурой. Этот шаг поможет нам установить базовую линию и увидеть, как программа работает как ожидается, прежде чем мы внесем какие - либо изменения.

```bash
cd ~/project/structly
python3 stock.py
```

Программа должна корректно запуститься и отобразить данные об акциях в отформатированной таблице. Если это так, значит, текущая структура кода работает без проблем с циклическими импортами.

Теперь мы изменим файл `formatter.py`. Обычно хорошей практикой является перемещение импортов в верхнюю часть файла. Это делает код более организованным и легче понять сразу.

```bash
cd ~/project/structly
```

Откройте файл `tableformat/formatter.py` в WebIDE. Мы переместим следующие импорты в верхнюю часть файла, сразу после существующих импортов. Эти импорты предназначены для различных форматеров таблиц, таких как текстовый, CSV и HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Теперь начало файла должно выглядеть так:

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

Сохраните файл и попробуйте запустить программу для работы с акциями снова.

```bash
python3 stock.py
```

Вы должны увидеть сообщение об ошибке о том, что `TableFormatter` не определен. Это явный признак проблемы с циклическим импортом.

Проблема возникает из - за следующей цепочки событий:

1. `formatter.py` пытается импортировать `TextTableFormatter` из `formats/text.py`.
2. `formats/text.py` импортирует `TableFormatter` из `formatter.py`.
3. Когда Python пытается разрешить эти импорты, он попадает в цикл, потому что не может решить, какой модуль импортировать полностью первым.

Вернем наши изменения, чтобы программа снова заработала. Отредактируйте файл `tableformat/formatter.py` и переместите импорты обратно в исходное место (после определения класса `TableFormatter`).

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

Запустите программу снова, чтобы убедиться, что она работает.

```bash
python3 stock.py
```

Это показывает, что даже если размещение импортов в середине файла не является наилучшей практикой с точки зрения организации кода, это было сделано, чтобы избежать проблемы с циклическим импортом. В следующих шагах мы рассмотрим лучшие решения.
