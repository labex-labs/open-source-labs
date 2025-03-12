# Финализация программы

Теперь мы собираемся очистить наш код и создать окончательную версию программы `pcost.py`. Очистка кода означает удаление всех ненужных частей и обеспечение хорошего вида вывода. Это важный шаг в программировании, так как делает наш код более профессиональным и легким для понимания.

Мы начнем с удаления отладочных инструкций вывода на экран. Эти инструкции используются во время разработки для проверки значений переменных и потока выполнения программы, но они не нужны в окончательной версии. Затем мы убедимся, что окончательный вывод имеет хороший формат.

Вот окончательная версия кода `pcost.py`:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
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

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

В этой окончательной версии кода есть несколько улучшений:

1. Обработка ошибок: Мы добавили код для перехвата двух типов ошибок. `FileNotFoundError` возникает, когда указанный файл не существует. В этом случае программа выведет сообщение об ошибке и вернет 0.0. Блок `Exception` перехватывает любые другие ошибки, которые могут возникнуть при обработке файла. Это делает нашу программу более надежной и менее склонной к неожиданным сбоям.
2. Корректный формат: Общая стоимость форматируется с двумя знаками после запятой с использованием спецификатора формата `:.2f` в f-строке. Это делает вывод более профессиональным и легким для чтения.
3. Проверка `__name__ == '__main__'`: Это распространенная идиома в Python. Она гарантирует, что код внутри блока `if` выполняется только при прямом запуске скрипта. Если скрипт импортируется как модуль в другой скрипт, этот код не будет выполняться. Это дает нам больше контроля над поведением нашего скрипта.

Теперь давайте запустим окончательный код. Откройте терминал и введите следующую команду:

```bash
python3 ~/project/pcost.py
```

При выполнении этой команды программа прочитает файл `portfolio.dat`, рассчитает общую стоимость портфеля и выведет результат. Вы должны увидеть общую стоимость портфеля, которая должна быть равна $44671.15.

Поздравляем! Вы успешно создали программу на Python, которая читает данные из файла, обрабатывает их и вычисляет результат. Это большой успех, и это показывает, что вы идете по пути к становлению опытным программистом на Python.
