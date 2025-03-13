# Разделение модуля для лучшей организации кода

По мере роста ваших Python - проектов вы, возможно, заметите, что один модульный файл становится очень большим и содержит несколько связанных, но различных компонентов. Когда это происходит, хорошей практикой является разделение модуля на пакет с подмодулями. Этот подход делает ваш код более организованным, легче поддерживаемым и масштабируемым.

## Понимание текущей структуры

Модуль `tableformat.py` представляет собой хороший пример большого модуля. Он содержит несколько классов - форматеров, каждый из которых отвечает за форматирование данных различным образом:

- `TableFormatter` (базовый класс): Это базовый класс для всех остальных классов - форматеров. Он определяет базовую структуру и методы, которые будут унаследованы и реализованы другими классами.
- `TextTableFormatter`: Этот класс форматирует данные в простом текстовом формате.
- `CSVTableFormatter`: Этот класс форматирует данные в формате CSV (Comma - Separated Values, значения, разделенные запятыми).
- `HTMLTableFormatter`: Этот класс форматирует данные в формате HTML (Hypertext Markup Language, язык гипертекстовой разметки).

Мы переорганизуем этот модуль в структуру пакета с отдельными файлами для каждого типа форматера. Это сделает код более модульным и легче управляемым.

## Шаг 1: Очистка кэш - файлов

Перед началом переорганизации кода хорошей идеей будет очистить все кэш - файлы Python. Эти файлы создаются Python для ускорения выполнения вашего кода, но они могут иногда вызывать проблемы при внесении изменений в код.

```bash
cd ~/project/structly
rm -rf __pycache__
```

В приведенных выше командах `cd ~/project/structly` изменяет текущую директорию на директорию `structly` в вашем проекте. `rm -rf __pycache__` удаляет директорию `__pycache__` и все ее содержимое. Опция `-r` означает рекурсивное удаление, то есть будут удалены все файлы и поддиректории внутри директории `__pycache__`. Опция `-f` означает принудительное удаление, то есть файлы будут удалены без запроса подтверждения.

## Шаг 2: Создание новой структуры пакета

Теперь давайте создадим новую структуру директорий для нашего пакета. Мы создадим директорию с именем `tableformat` и поддиректорию с именем `formats` внутри нее.

```bash
mkdir -p tableformat/formats
```

Команда `mkdir` используется для создания директорий. Опция `-p` означает создание всех необходимых родительских директорий, если они не существуют. Таким образом, если директория `tableformat` не существует, она будет создана сначала, а затем внутри нее будет создана директория `formats`.

## Шаг 3: Перемещение и переименование исходного файла

Далее мы переместим исходный файл `tableformat.py` в новую структуру и переименуем его в `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

Команда `mv` используется для перемещения или переименования файлов. В данном случае мы перемещаем файл `tableformat.py` в директорию `tableformat` и переименовываем его в `formatter.py`.

## Шаг 4: Разделение кода на отдельные файлы

Теперь нам нужно создать файлы для каждого форматера и переместить в них соответствующий код.

### 1. Создание файла базового форматера

```bash
touch tableformat/formatter.py
```

Команда `touch` используется для создания пустого файла. В данном случае мы создаем файл с именем `formatter.py` в директории `tableformat`.

Мы сохраним базовый класс `TableFormatter` и любые общие вспомогательные функции, такие как `print_table` и `create_formatter`, в этом файле. Файл должен выглядеть примерно так:

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

Переменная `__all__` используется для указания, какие символы должны быть импортированы при использовании `from module import *`. В данном случае мы указываем, что должны быть импортированы только символы `TableFormatter`, `print_table` и `create_formatter`.

Класс `TableFormatter` является базовым классом для всех остальных классов - форматеров. Он определяет два метода, `headings` и `row`, которые должны быть реализованы подклассами.

Функция `print_table` - это вспомогательная функция, которая принимает список объектов, список имен столбцов и объект - форматер и выводит данные в отформатированной таблице.

Функция `create_formatter` - это фабричная функция, которая принимает имя формата в качестве аргумента и возвращает соответствующий объект - форматер.

Сохраните файл и выйдите из редактора после внесения этих изменений.

### 2. Создание текстового форматера

```bash
touch tableformat/formats/text.py
```

Мы добавим только класс `TextTableFormatter` в этот файл.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Переменная `__all__` указывает, что при использовании `from module import *` должен быть импортирован только символ `TextTableFormatter`.

Инструкция `from ..formatter import TableFormatter` импортирует класс `TableFormatter` из файла `formatter.py` в родительской директории.

Класс `TextTableFormatter` наследуется от класса `TableFormatter` и реализует методы `headings` и `row` для форматирования данных в простом текстовом формате.

Сохраните файл и выйдите из редактора после внесения этих изменений.

### 3. Создание CSV - форматера

```bash
touch tableformat/formats/csv.py
```

Мы добавим только класс `CSVTableFormatter` в этот файл.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

Подобно предыдущим шагам, мы указываем переменную `__all__`, импортируем класс `TableFormatter` и реализуем методы `headings` и `row` для форматирования данных в формате CSV.

Сохраните файл и выйдите из редактора после внесения этих изменений.

### 4. Создание HTML - форматера

```bash
touch tableformat/formats/html.py
```

Мы добавим только класс `HTMLTableFormatter` в этот файл.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Снова мы указываем переменную `__all__`, импортируем класс `TableFormatter` и реализуем методы `headings` и `row` для форматирования данных в формате HTML.

Сохраните файл и выйдите из редактора после внесения этих изменений.

## Шаг 5: Создание файлов инициализации пакета

В Python файлы `__init__.py` используются для пометки директорий как Python - пакетов. Мы должны создать файлы `__init__.py` как в директории `tableformat`, так и в директории `formats`.

### 1. Создание файла для пакета `tableformat`

```bash
touch tableformat/__init__.py
```

Добавьте следующее содержимое в файл:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Эта инструкция импортирует все символы из файла `formatter.py` и делает их доступными при импорте пакета `tableformat`.

Сохраните файл и выйдите из редактора после внесения этих изменений.

### 2. Создание файла для пакета `formats`

```bash
touch tableformat/formats/__init__.py
```

Вы можете оставить этот файл пустым или добавить простую строки документации (docstring):

```python
'''
Format implementations for different output formats.
'''
```

Строка документации дает краткое описание того, что делает пакет `formats`.

Сохраните файл и выйдите из редактора после внесения этих изменений.

## Шаг 6: Тестирование новой структуры

Давайте создадим простой тест, чтобы убедиться, что наши изменения работают правильно.

```bash
cd ~/project
touch test_tableformat.py
```

Добавьте следующее содержимое в файл `test_tableformat.py`:

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

Этот тестовый код импортирует необходимые функции и классы из пакета `structly`, создает форматеры каждого типа, определяет некоторые тестовые данные и затем тестирует каждый форматер, выводя данные в соответствующем формате.

Сохраните файл и выйдите из редактора после внесения этих изменений. Теперь запустите тест:

```bash
python test_tableformat.py
```

Вы должны увидеть одни и те же данные, отформатированные тремя разными способами (текстом, CSV и HTML). Если вы видите ожидаемый вывод, это означает, что переорганизация вашего кода прошла успешно.
