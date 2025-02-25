# Общие习惯用法 для записи в файл

Записать строковые данные.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

Перенаправить функцию print.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

Эти упражнения зависят от файла `portfolio.csv`. Файл содержит список строк с информацией о портфеле акций. Предполагается, что вы работаете в каталоге `~/project/`. Если вы не уверены, вы можете узнать, где Python считает, что он запущен, выполнив это:

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # Output vary
>>>
```
