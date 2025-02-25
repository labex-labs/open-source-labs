# Примерная программа

Решим следующую задачу:

> Однажды утром вы вышли на улицу и положили доллар на тротуар у Сирс-башни в Чикаго. Каждый день после этого вы вышли на улицу и удваивали количество купюр. Через сколько дней количество купюр превысит высоту башни?

Вот решение, которое заключается в создании файла `sears.py` в директории `/home/labex/project`:

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Когда вы запускаете его, получаете следующий вывод:

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Number of days 23
Number of bills 4194304
Final height 461.37344
```

С использованием этой программы в качестве руководства вы можете изучить ряд важных основных концепций языка Python.
