# Обработка данных

Теперь, когда мы научились читать файл, следующим шагом является обработка каждой строки файла для расчета стоимости каждой покупки акций. Это важная часть работы с данными в Python, так как позволяет извлекать значимую информацию из файла.

Каждая строка в файле имеет определенный формат: `[Тикер акции] [Количество акций] [Цена за одну акцию]`. Чтобы рассчитать стоимость каждой покупки акций, нам нужно извлечь количество акций и цену за одну акцию из каждой строки. Затем мы умножаем эти два значения друг на друга, чтобы получить стоимость данной покупки акций. Наконец, мы добавляем эту стоимость к накопленной общей сумме, чтобы найти общую стоимость портфеля.

Давайте модифицируем функцию `portfolio_cost()` в файле `pcost.py`, чтобы достичь этого. Вот модифицированный код:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into fields
            fields = line.split()

            # Extract the relevant data
            # fields[0] is the stock symbol (which we don't need for the calculation)
            shares = int(fields[1])  # Number of shares (second field)
            price = float(fields[2])  # Price per share (third field)

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

Разберем, что делает эта модифицированная функция шаг за шагом:

1. **Удаление пробелов**: Мы используем метод `strip()`, чтобы удалить все ведущие и завершающие пробелы из каждой строки. Это гарантирует, что при разделении строки на поля мы не случайно включим лишние пробелы.
2. **Пропуск пустых строк**: Если строка пуста (то есть содержит только пробелы), мы используем оператор `continue`, чтобы пропустить ее. Это помогает избежать ошибок при попытке разделить пустую строку.
3. **Разделение строки на поля**: Мы используем метод `split()`, чтобы разделить каждую строку на список полей на основе пробелов. Это позволяет нам отдельно обращаться к каждой части строки.
4. **Извлечение нужных данных**: Мы извлекаем количество акций и цену за одну акцию из списка полей. Количество акций - это второе поле, а цена за одну акцию - третье поле. Мы преобразуем эти значения в соответствующие типы данных (`int` для количества акций и `float` для цены), чтобы можно было выполнять арифметические операции с ними.
5. **Расчет стоимости**: Мы умножаем количество акций на цену за одну акцию, чтобы рассчитать стоимость данной покупки акций.
6. **Добавление к общей сумме**: Мы добавляем стоимость данной покупки акций к накопленной общей стоимости.
7. **Вывод отладочной информации**: Мы выводим некоторую информацию о каждой покупке акций, чтобы видеть, что происходит. Это включает в себя тикер акции, количество акций, цену за одну акцию и общую стоимость покупки.

Теперь давайте запустим код, чтобы проверить, работает ли он. Откройте терминал и выполните следующую команду:

```bash
python3 ~/project/pcost.py
```

После выполнения команды вы должны увидеть подробную информацию о каждой покупке акций, за которой следует общая стоимость портфеля. Этот вывод поможет вам убедиться, что функция работает правильно и что вы корректно рассчитали общую стоимость.
