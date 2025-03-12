# Реализация валидации свойств

Свойства (properties) в Python - это мощный инструмент. Они не только позволяют получать вычисляемые значения так, как если бы это были обычные атрибуты, но и дают возможность контролировать, как эти значения атрибутов извлекаются, устанавливаются и удаляются. Этот контроль чрезвычайно полезен, когда необходимо добавить валидацию для атрибутов. Валидация гарантирует, что значения, присваиваемые атрибутам, соответствуют определенным критериям, что помогает сохранить целостность данных.

В нашем классе `Stock` есть два важных атрибута: `shares` и `price`. Мы хотим убедиться, что `shares` - это неотрицательное целое число, а `price` - неотрицательное число с плавающей точкой. Чтобы реализовать такую валидацию, мы будем использовать декораторы свойств вместе с геттерами и сеттерами.

## Инструкции:

1. Сначала вам нужно открыть файл `stock.py` в редакторе. Именно здесь мы будем вносить все изменения в наш класс `Stock`. Используйте следующую команду в терминале:

   ```bash
   code /home/labex/project/stock.py
   ```

2. В Python можно использовать приватные атрибуты для хранения фактических значений переменных класса. Приватные атрибуты обозначаются подчеркиванием в начале имени. Добавьте приватные атрибуты `_shares` и `_price` в класс `Stock` и измените конструктор, чтобы он использовал их. Конструктор - это метод, который вызывается при создании нового экземпляра класса. Вот как это сделать:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. Теперь мы определим свойства для `shares` и `price` с правильной валидацией. Свойства определяются с использованием декоратора `@property` для геттер - метода и декоратора `@<property_name>.setter` для сеттер - метода. Геттер - метод используется для получения значения атрибута, а сеттер - метод - для его установки. Вот код для добавления определений свойств с валидацией:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, int):
           raise TypeError("Expected integer")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, float):
           raise TypeError("Expected float")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

4. Обновите конструктор, чтобы он использовал сеттеры свойств для валидации. Таким образом, каждый раз при создании нового экземпляра класса `Stock` значения `shares` и `price` будут автоматически валидироваться. Вот обновленный конструктор:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. После внесения всех этих изменений сохраните файл `stock.py`. Это гарантирует, что ваши изменения будут сохранены.

6. Чтобы убедиться, что наша валидация работает правильно, мы создадим тестовый скрипт. Откройте новый файл с именем `test_validation.py` в редакторе с помощью следующей команды:

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. Добавьте следующий код в файл `test_validation.py`. Этот код создает корректный экземпляр класса `Stock`, а затем пытается обновить атрибуты `shares` и `price` как корректными, так и некорректными значениями. Он также выводит результаты и любые сообщения об ошибках, которые могут возникнуть.

   ```python
   from stock import Stock

   # Create a valid stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

   # Test valid updates
   try:
       s.shares = 50  # Valid update
       print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting shares=50: {e}")

   try:
       s.price = 123.45  # Valid update
       print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting price=123.45: {e}")

   # Test invalid updates
   try:
       s.shares = "50"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares='50': {e}")

   try:
       s.shares = -10  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares=-10: {e}")

   try:
       s.price = "123.45"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price='123.45': {e}")

   try:
       s.price = -10.0  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price=-10.0: {e}")
   ```

8. Наконец, запустите тестовый скрипт с помощью следующей команды в терминале:
   ```bash
   python /home/labex/project/test_validation.py
   ```

Вы должны увидеть вывод, показывающий успешные корректные обновления и соответствующие сообщения об ошибках для некорректных обновлений. Это подтверждает, что наша валидация свойств работает как ожидается.
