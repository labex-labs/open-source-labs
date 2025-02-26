# Добавление дополнительных реализаций

Создайте класс `CSVTableFormatter`, который позволяет генерировать вывод в формате CSV:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.CSVTableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
>>>
```

Создайте класс `HTMLTableFormatter`, который генерирует вывод в формате HTML:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.HTMLTableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```
