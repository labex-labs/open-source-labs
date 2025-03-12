# Создание пользовательского контейнерного класса

В обработке данных столбцовая организация данных отлично подходит для экономии памяти. Однако это может вызвать проблемы, если существующий код предполагает, что данные представлены в виде списка словарей. Чтобы решить эту проблему, мы создадим пользовательский контейнерный класс. Этот класс предоставит интерфейс строковой организации данных, то есть для кода он будет выглядеть и вести себя как список словарей. Но внутренне он будет хранить данные в столбцовом формате, что поможет нам сэкономить память.

1. Сначала откройте файл `readrides.py` в редакторе WebIDE. Мы добавим новый класс в этот файл. Этот класс станет основой нашего пользовательского контейнера.

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

В этом коде мы определяем класс с именем `RideData`, который наследуется от `Sequence`. Метод `__init__` инициализирует четыре пустых списка, каждый из которых представляет столбец данных. Метод `__len__` возвращает длину контейнера, которая равна длине списка `routes`. Метод `__getitem__` позволяет получить доступ к конкретной записи по индексу, возвращая ее в виде словаря. Метод `append` добавляет новую запись в контейнер, добавляя значения в каждый столбцовый список.

2. Теперь нам нужна функция для чтения данных о поездках на автобусах в наш пользовательский контейнер. Добавьте следующую функцию в файл `readrides.py`.

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Эта функция создает экземпляр класса `RideData` и заполняет его данными из CSV-файла. Она читает каждую строку из файла, извлекает соответствующую информацию, создает словарь для каждой записи и затем добавляет его в контейнер `RideData`. Главное, что она сохраняет тот же интерфейс, что и список словарей, но внутренне хранит данные по столбцам.

3. Давайте протестируем наш пользовательский контейнер в оболочке Python. Это поможет нам убедиться, что он работает как ожидается.

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

Наш пользовательский контейнер успешно реализует интерфейс `Sequence`, что означает, что он ведет себя как список. Вы можете использовать функцию `len()` для получения количества записей в контейнере, и вы можете использовать индексацию для доступа к отдельным записям. Каждая запись выглядит как словарь, даже если данные хранятся по столбцам внутренне. Это замечательно, потому что существующий код, который предполагает список словарей, будет продолжать работать с нашим пользовательским контейнером без каких - либо изменений.

4. Наконец, давайте измерим использование памяти нашего пользовательского контейнера. Это покажет, сколько памяти мы экономим по сравнению со списком словарей.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

Когда вы запустите этот код, вы должны увидеть, что использование памяти похоже на столбцовую организацию данных, которое намного меньше, чем использование памяти списком словарей. Это демонстрирует преимущество нашего пользовательского контейнера с точки зрения эффективности использования памяти.
