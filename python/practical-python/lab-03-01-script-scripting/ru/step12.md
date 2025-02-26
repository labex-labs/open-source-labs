# Упражнение 3.2: Создание верхнего уровня функции для выполнения программы

Возьмите последнюю часть вашей программы и упакуйте ее в отдельную функцию `portfolio_report(portfolio_filename, prices_filename)`. Сделайте так, чтобы вызов этой функции создавал отчет как и раньше:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

В этой окончательной версии ваша программа будет состоять только из серии определений функций, за которыми следует единственный вызов функции `portfolio_report()` в конце (который выполняет все шаги, связанные с программой).

Преобразовав вашу программу в отдельную функцию, становится легко запускать ее с разными входными данными. Например, попробуйте эти инструкции интерактивно после запуска вашей программы:

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... look at the output...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... look at the output...
>>>
```
