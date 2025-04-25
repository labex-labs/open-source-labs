# 演習 3.7: 異なる列区切り文字の選択

CSV ファイルは非常に一般的ですが、タブやスペースなど、異なる列区切り文字を使用するファイルに遭遇する可能性もあります。たとえば、`portfolio.dat` ファイルは次のようになっています。

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

`csv.reader()` 関数を使用すると、次のように異なる列区切り文字を指定できます。

```python
rows = csv.reader(f, delimiter=' ')
```

`/home/labex/project/fileparse_3.7.py` の `parse_csv()` 関数を修正して、区切り文字の変更も可能にしましょう。

たとえば：

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
