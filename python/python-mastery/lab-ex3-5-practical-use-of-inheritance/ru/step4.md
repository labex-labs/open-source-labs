# Создание дополнительных форматеров

В программировании наследование представляет собой мощную концепцию, которая позволяет создавать новые классы на основе существующих. Это помогает повторно использовать код и делает наши программы более расширяемыми. В этой части эксперимента мы воспользуемся наследованием для создания двух новых форматеров для разных форматов вывода: CSV и HTML. Эти форматеры будут наследоваться от базового класса, что означает, что они будут иметь общий набор поведений, но при этом будут иметь свои уникальные способы форматирования данных.

Теперь добавим следующие классы в файл `tableformat.py`. Эти классы определят, как форматировать данные в форматах CSV и HTML соответственно.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

Класс `CSVTableFormatter` предназначен для форматирования данных в формате CSV (Comma - Separated Values, значения, разделенные запятыми). Метод `headings` принимает список заголовков и выводит их, разделенных запятыми. Метод `row` принимает список данных для одной строки и также выводит их, разделенных запятыми.

Класс `HTMLTableFormatter`, напротив, используется для генерации HTML - кода таблицы. Метод `headings` создает заголовки таблицы с использованием HTML - тегов `<th>`, а метод `row` создает строку таблицы с использованием HTML - тегов `<td>`.

Протестируем эти новые форматеры, чтобы увидеть, как они работают.

1. Сначала протестируем CSV - форматер:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

В этом коде мы сначала импортируем необходимые модули. Затем мы читаем данные из CSV - файла с именем `portfolio.csv` и создаем экземпляры класса `Stock`. Далее мы создаем экземпляр класса `CSVTableFormatter`. Наконец, мы используем функцию `print_table` для вывода данных о портфеле в формате CSV.

Вы должны увидеть следующий вывод в формате CSV:

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Теперь протестируем HTML - форматер:

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Здесь мы создаем экземпляр класса `HTMLTableFormatter` и снова используем функцию `print_table` для вывода данных о портфеле в формате HTML.

Вы должны увидеть следующий вывод в формате HTML:

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Как вы можете видеть, каждый форматер создает вывод в разном формате, но все они используют один и тот же интерфейс, определенный базовым классом `TableFormatter`. Это отличный пример мощности наследования и полиморфизма. Мы можем писать код, который работает с базовым классом, и он автоматически будет работать с любым подклассом.

Функция `print_table()` не нуждается в знании о конкретном используемом форматере. Она просто вызывает методы, определенные в базовом классе, и соответствующая реализация выбирается на основе типа предоставленного форматера. Это делает наш код более гибким и легким в поддержке.
