# Глубокая идея: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) - это концепция компьютерного программирования для определения, может ли объект быть использован для определенной цели. Это приложение [теста утки](https://en.wikipedia.org/wiki/Duck_test).

> Если оно выглядит как утка, плавает как утка и крякает как утка, то, вероятно, это утка.

Во второй версии `read_data()` выше функция ожидает любого итерируемого объекта. Не только строки файла.

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

Это означает, что мы можем использовать его с другими _строками_.

```python
# CSV-файл
lines = open('data.csv')
data = read_data(lines)

# Архивированный файл
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# Стандартный ввод
lines = sys.stdin
data = read_data(lines)

# Список строк
lines = ['ACME,50,91.1','IBM,75,123.45',...]
data = read_data(lines)
```

В этом дизайне есть значительная гибкость.

_Вопрос: Следует ли мы принимать или бороться с этой гибкостью?_
