# Реализация регистрации подклассов

В программировании циклические импорты могут быть сложной проблемой. Вместо прямого импорта классов форматеров мы можем использовать паттерн регистрации. В этом паттерне подклассы регистрируются у своего родительского класса. Это распространенный и эффективный способ избежать циклических импортов.

Сначала разберемся, как можно узнать имя модуля класса. Имя модуля важно, так как мы будем использовать его в нашем паттерне регистрации. Для этого выполним команду Python в терминале.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

При выполнении этой команды вы увидите такой вывод:

```
structly.tableformat.formats.text
text
```

Этот вывод показывает, что мы можем извлечь имя модуля из самого класса. Мы будем использовать это имя модуля позже для регистрации подклассов.

Теперь изменим класс `TableFormatter` в файле `tableformat/formatter.py`, чтобы добавить механизм регистрации. Откройте этот файл в WebIDE. Мы добавим некоторый код в класс `TableFormatter`. Этот код поможет нам автоматически регистрировать подклассы.

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Метод `__init_subclass__` - это специальный метод в Python. Он вызывается каждый раз, когда создается подкласс `TableFormatter`. В этом методе мы извлекаем имя модуля подкласса и используем его в качестве ключа для регистрации подкласса в словаре `_formats`.

Далее нам нужно изменить функцию `create_formatter`, чтобы использовать словарь регистрации. Эта функция отвечает за создание соответствующего форматера на основе заданного имени.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
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

После внесения этих изменений сохраните файл. Затем проверим, работает ли программа. Мы запустим скрипт `stock.py`.

```bash
python3 stock.py
```

Если программа запускается корректно, значит, наши изменения не сломали ничего. Теперь посмотрим на содержимое словаря `_formats`, чтобы увидеть, как работает регистрация.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

Вы должны увидеть такой вывод:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

Этот вывод подтверждает, что наши подклассы корректно регистрируются в словаре `_formats`. Однако у нас все еще есть некоторые импорты в середине файла. На следующем шаге мы исправим эту проблему с помощью динамических импортов.
