# Упражнение 2.11: Добавление заголовков

Предположим, у вас есть кортеж имен заголовков, такой как:

```python
headers = ('Name', 'Shares', 'Price', 'Change')
```

Добавьте в программу код, который берет вышеуказанный кортеж заголовков и создает строку, в которой каждое имя заголовка выравнивается по правому краю в поле шириной в 10 символов, а каждый столбец разделяется одним пробелом.

```python
'      Name     Shares      Price      Change'
```

Напишите код, который берет заголовки и создает строку-разделитель между заголовками и последующими данными. Эта строка состоит из набора символов "-" под каждым именем поля. Например:

```python
'---------- ---------- ---------- -----------'
```

После завершения работы программа должна выводить таблицу, показанную в начале этого упражнения.

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84
