# Упражнение 1.6: Дебагинг

Следующий фрагмент кода содержит код из задачи с башней Сирс. В нем также есть ошибка.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Скопируйте и вставьте код, приведенный выше, в новый файл под названием `sears.py`. Когда вы запустите код, вы получите сообщение об ошибке, из-за которого программа будет аварийно завершаться так:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Чтение сообщений об ошибках - важная часть работы с кодом на Python. Если ваша программа завершается аварийно, последняя строка сообщения трассировки ошибки - это фактическая причина аварийного завершения программы. Выше этого вы должны увидеть фрагмент исходного кода, а затем имя файла и номер строки, идентифицирующие ошибку.

- Какой строке принадлежит ошибка?
- Какая ошибка?
- Исправьте ошибку
- Запустите программу успешно
