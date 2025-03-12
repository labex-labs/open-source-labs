# Реализация миксин-классов для форматирования

На этом этапе мы узнаем о миксин-классах (mixin classes). Миксин-классы - это очень полезная техника в Python. Они позволяют добавлять дополнительную функциональность классам без изменения их исходного кода. Это замечательно, так как помогает сделать код модульным и легко управляемым.

## Что такое миксин-классы?

Миксин - это особый тип класса. Его основная цель - предоставить некоторую функциональность, которую может наследовать другой класс. Однако миксин не предназначен для самостоятельного использования. Вы не создаете экземпляр миксин-класса напрямую. Вместо этого вы используете его для добавления определенных функций к другим классам контролируемым и предсказуемым способом. Это форма множественного наследования, когда класс может наследовать от нескольких родительских классов.

Теперь реализуем два миксин-класса в файле `tableformat.py`. Сначала откройте файл в редакторе. Это можно сделать, запустив следующие команды в терминале:

```bash
cd ~/project
code tableformat.py
```

После открытия файла добавьте следующие определения классов в конец файла, но до любых существующих функций.

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Класс `ColumnFormatMixin` предоставляет функциональность форматирования столбцов. Классовая переменная `formats` представляет собой список, содержащий коды форматирования. Эти коды используются для форматирования данных в каждом столбце. Метод `row()` принимает данные строки, применяет коды форматирования к каждому элементу строки, а затем передает отформатированные данные строки родительскому классу с помощью `super().row(rowdata)`.

Далее добавьте еще один миксин-класс, который делает заголовки таблицы заглавными:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Класс `UpperHeadersMixin` преобразует текст заголовков в верхний регистр. Он принимает список заголовков, преобразует каждый заголовок в верхний регистр, а затем передает измененные заголовки методу `headings()` родительского класса с помощью `super().headings()`.

## Использование миксин-классов

Протестируем наши новые миксин-классы. Запустим некоторый Python-код, чтобы увидеть, как они работают.

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

При запуске этого кода вы должны увидеть красиво отформатированный вывод. Столбец с ценами будет иметь единообразное количество десятичных знаков благодаря форматированию, предоставляемому классом `ColumnFormatMixin`.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Теперь попробуем класс `UpperHeadersMixin`. Запустите следующий код:

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Этот код должен отобразить заголовки в верхнем регистре.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## Понимание кооперативного наследования

Обратите внимание, что в наших миксин-классах мы используем `super().method()`. Это называется "кооперативным наследованием". В кооперативном наследовании каждый класс в цепочке наследования работает вместе. Когда класс вызывает `super().method()`, он просит следующий класс в цепочке выполнить свою часть задачи. Таким образом, цепочка классов может добавлять свою собственную функциональность к общему процессу.

Порядок наследования очень важен. Когда мы определяем `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)`, Python ищет методы сначала в `ColumnFormatMixin`, а затем в `TextTableFormatter`. Поэтому, когда в `ColumnFormatMixin` вызывается `super().row()`, это ссылается на `TextTableFormatter.row()`.

Мы даже можем комбинировать оба миксин-класса. Запустите следующий код:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Этот код даст нам и заглавные заголовки, и отформатированные числа.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

На следующем этапе мы сделаем использование этих миксин-классов более удобным, улучшив функцию `create_formatter()`.
