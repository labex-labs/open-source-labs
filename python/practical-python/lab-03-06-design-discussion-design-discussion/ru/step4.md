# Упражнение 3.17: От имен файлов до объектов, подобных файлам

Теперь вы создали файл `fileparse.py`, в котором содержалась функция `parse_csv()`. Функция работала так:

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

В настоящее время функция ожидает, что ей передадут имя файла. Однако вы можете сделать код более гибким. Измените функцию так, чтобы она работала с любым объектом, подобным файлу/итерируемым объектом. Например:

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

В этом новом коде что произойдет, если вы передадите имя файла, как раньше?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... посмотрите на вывод (он должен быть странным)...
>>>
```

Да, вам нужно быть осторожными. Возможно, вы можете добавить проверку безопасности, чтобы избежать этого?
