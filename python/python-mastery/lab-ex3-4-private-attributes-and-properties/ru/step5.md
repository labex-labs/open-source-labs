# Согласование валидации типов с переменными класса

В нашей Python - программе мы создали класс `Stock`. В настоящее время этот класс имеет два разных способа обработки типов данных. Понимание этих механизмов является важным, так как это помогает нам лучше управлять и организовывать наш код.

Первый механизм - это переменная класса `_types`. Эта переменная используется для преобразования данных из строк. Когда мы получаем данные в формате строки, переменная `_types` помогает нам преобразовать эти данные в соответствующие типы для нашего класса `Stock`.

Второй механизм - это сеттеры свойств. Эти сеттеры обеспечивают проверку типов. Каждый раз, когда мы пытаемся установить значение для свойства в нашем классе `Stock`, сеттеры свойств гарантируют, что значение имеет правильный тип.

Однако наличие двух отдельных механизмов может сделать наш класс сложным в поддержке. Чтобы решить эту проблему, нам нужно согласовать эти два механизма так, чтобы они использовали одну и ту же информацию о типах. Таким образом, мы обеспечиваем согласованность в нашем классе, и он становится более надежным при создании подклассов.

## Инструкции:

1. Сначала нам нужно открыть файл `stock.py` в редакторе. Этот файл содержит код нашего класса `Stock`. Чтобы открыть его, выполните следующую команду в терминале:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Теперь мы изменим сеттеры свойств в файле `stock.py`. Мы хотим, чтобы они использовали типы, определенные в переменной класса `_types`. Это гарантирует, что проверка типов в сеттерах свойств совпадает с преобразованием типов, выполняемым переменной `_types`. Вот как мы модифицируем сеттеры свойств:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, self._types[1]):
           raise TypeError(f"Expected {self._types[1].__name__}")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, self._types[2]):
           raise TypeError(f"Expected {self._types[2].__name__}")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

3. После внесения этих изменений сохраните файл `stock.py`. Сохранение файла гарантирует, что наши изменения будут сохранены.

4. Далее мы создадим тестовый скрипт, чтобы убедиться, что создание подклассов с разными типами работает как ожидается. Чтобы создать этот скрипт, выполните следующую команду в терминале:

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. Теперь добавьте следующий код в файл `test_subclass.py`. Этот код создает подкласс класса `Stock` с разными типами и тестирует как базовый класс, так и подкласс.

   ```python
   from stock import Stock
   from decimal import Decimal

   # Create a subclass with different types
   class DStock(Stock):
       _types = (str, int, Decimal)

   # Test the base class
   s = Stock('GOOG', 100, 490.10)
   print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

   # Test valid update with float
   try:
       s.price = 500.25
       print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
   except Exception as e:
       print(f"Error updating Stock price: {e}")

   # Test the subclass with Decimal
   ds = DStock('AAPL', 50, Decimal('142.50'))
   print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

   # Test invalid update with float (should require Decimal)
   try:
       ds.price = 150.75
       print(f"Updated DStock price: {ds.price}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")

   # Test valid update with Decimal
   try:
       ds.price = Decimal('155.25')
       print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")
   ```

6. Наконец, запустите тестовый скрипт, чтобы увидеть результаты. Выполните следующую команду в терминале:

   ```bash
   python /home/labex/project/test_subclass.py
   ```

При запуске тестового скрипта вы должны увидеть, что базовый класс `Stock` принимает значения с плавающей точкой для цены, в то время как подкласс `DStock` требует значения типа `Decimal`. Это показывает, что наше согласование типов работает как ожидается.

### Обсуждение

Согласовав информацию о типах в нашем классе `Stock`, мы сделали класс более согласованным. Теперь сеттеры свойств используют ту же информацию о типах, что и метод `from_row`. Эта согласованность делает класс легче в поддержке и расширении, особенно при создании подклассов.

Хотя текущая реализация нашего класса `Stock` может показаться сложной для простой концепции, она демонстрирует важные техники Python для инкапсуляции и безопасности типов. В реальных приложениях вы, возможно, захотите использовать более продвинутые инструменты, такие как датаклассы (dataclasses) или сторонние библиотеки, чтобы упростить такую реализацию. Эти инструменты могут сделать ваш код более компактным и легким в управлении.
