# Создание класса Ticker

При обработке данных работа с сырыми данными может быть весьма сложной. Чтобы сделать нашу работу с данными о ценах на акции более организованной и эффективной, мы определим соответствующий класс для представления котировок акций. Этот класс станет шаблоном для наших данных о ценах на акции, сделав наш конвейер обработки данных более надежным и легким в управлении.

## Создание файла ticker.py

1. Сначала нам нужно создать новый файл в WebIDE. Вы можете сделать это, нажав на иконку "New File" или щелкнув правой кнопкой мыши в проводнике файлов и выбрав "New File". Назовите этот файл `ticker.py`. В этом файле будет находиться код нашего класса `Ticker`.

2. Теперь добавим следующий код в только что созданный файл `ticker.py`. Этот код определит наш класс `Ticker` и настроит простой конвейер обработки данных для его тестирования.

```python
# ticker.py

from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. После добавления кода сохраните файл. Вы можете сделать это, нажав `Ctrl+S` или выбрав "File" → "Save" в меню. Сохранение файла гарантирует, что ваши изменения будут сохранены и можно будет запустить код позже.

## Понимание кода

Рассмотрим, что делает этот код пошагово:

1. В начале кода мы импортируем класс `Structure` и типы полей из модуля `structure.py`. Этот модуль уже настроен для вас. Эти импорты важны, так как они предоставляют строительные блоки для нашего класса `Ticker`. Класс `Structure` станет базовым классом для нашего класса `Ticker`, а типы полей, такие как `String`, `Float` и `Integer`, определят типы данных полей наших данных о ценах на акции.

2. Затем мы определяем класс `Ticker`, который наследуется от `Structure`. Этот класс имеет несколько полей, которые представляют различные аспекты данных о ценах на акции:
   - `name`: Это поле хранит тикер акции, например, "IBM" или "AAPL". Оно помогает нам определить, акции какой компании мы обрабатываем.
   - `price`: Оно хранит текущую цену акции. Это важная информация для инвесторов.
   - `date` и `time`: Эти поля показывают, когда была сгенерирована котировка акции. Знание времени и даты важно для анализа тенденций изменения цен на акции в течение времени.
   - `change`: Это представляет изменение цены акции. Оно показывает, выросла ли цена акции или упала по сравнению с предыдущим значением.
   - `open`, `high`, `low`: Эти поля представляют цену открытия, максимальную цену и минимальную цену акции за определенный период. Они дают нам представление о диапазоне цен акции.
   - `volume`: Это поле хранит количество проданных акций. Высокий объем торгов может указывать на сильный интерес рынка к определенной акции.

3. В блоке `if __name__ == '__main__':` мы настраиваем конвейер обработки данных. Этот блок кода будет выполнен, когда мы запустим файл `ticker.py` напрямую.
   - `follow('stocklog.csv')` - это функция, которая генерирует строки из файла `stocklog.csv`. Она позволяет нам читать файл построчно.
   - `csv.reader(lines)` принимает эти строки и разбирает их на строки данных. CSV (Comma - Separated Values) - это распространенный формат файлов для хранения табличных данных, и эта функция помогает нам извлечь данные из каждой строки.
   - `(Ticker.from_row(row) for row in rows)` - это выражение - генератор. Оно принимает каждую строку данных и преобразует ее в объект `Ticker`. Таким образом, мы преобразуем сырые данные в формате CSV в структурированные объекты, с которыми легче работать.
   - Цикл `for` проходит по этим объектам `Ticker` и выводит каждый из них. Это позволяет нам увидеть структурированные данные в действии.

## Запуск кода

Запустим код, чтобы увидеть, как он работает:

1. Сначала убедимся, что мы находимся в директории проекта в терминале. Если вы еще не там, используйте следующую команду, чтобы перейти в нее:

   ```bash
   cd /home/labex/project
   ```

2. Когда вы находитесь в правильной директории, запустите скрипт `ticker.py` с помощью следующей команды:

   ```bash
   python3 ticker.py
   ```

3. После запуска скрипта вы должны увидеть вывод, похожий на следующий (ваши данные могут отличаться):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

Вы можете остановить выполнение скрипта, нажав `Ctrl+C`, когда увидите достаточно вывода.

Обратите внимание, как сырые данные в формате CSV были преобразованы в структурированные объекты `Ticker`. Это преобразование делает данные намного легче обрабатывать в нашем конвейере обработки данных, так как теперь мы можем обращаться к данным о ценах на акции и манипулировать ими с помощью полей, определенных в классе `Ticker`.
