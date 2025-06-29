# Comparando Diferentes Estruturas de Dados

Em Python, as estruturas de dados são usadas para organizar e armazenar dados relacionados. Elas são como contêineres que contêm diferentes tipos de informações de forma estruturada. Nesta etapa, compararemos diferentes estruturas de dados e veremos quanta memória elas usam.

Vamos criar um novo arquivo chamado `compare_structures.py` no diretório `/home/labex/project`. Este arquivo conterá o código para ler dados de um arquivo CSV e armazená-los em diferentes estruturas de dados.

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# Define a named tuple for rides data
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# A named tuple is a lightweight class that allows you to access its fields by name.
# It's like a tuple, but with named attributes.

# Define a class with __slots__ for memory optimization
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__ is a memory - optimized class.
# It avoids using an instance dictionary, which saves memory.

# Define a regular class for rides data
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A regular class is an object - oriented way to represent data.
# It has named attributes and can have methods.

# Function to read data as tuples
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as tuples.
# Tuples are immutable sequences, and you access their elements by numeric index.

# Function to read data as dictionaries
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as dictionaries.
# Dictionaries use key - value pairs, so you can access elements by their names.

# Function to read data as named tuples
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as named tuples.
# Named tuples combine the efficiency of tuples with the readability of named access.

# Function to read data as regular class instances
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a regular class.
# Regular classes allow you to add methods to your data.

# Function to read data as slotted class instances
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a slotted class.
# Slotted classes are memory - optimized and still provide named access.

# Function to measure memory usage
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # Demonstrate how to use each data structure
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # named tuples and classes
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # Run all memory tests
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # Sort by memory usage (lowest first)
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

Execute o script para ver os resultados da comparação:

```bash
python3 /home/labex/project/compare_structures.py
```

A saída mostrará o uso de memória para cada estrutura de dados, juntamente com uma classificação da mais para a menos eficiente em termos de memória.

## Compreendendo as Diferentes Estruturas de Dados

1.  **Tuplas**:
    - Tuplas são sequências leves e imutáveis. Isso significa que, uma vez que você cria uma tupla, não pode alterar seus elementos.
    - Você acessa elementos em uma tupla por seu índice numérico, como `record[0]`, `record[1]`, etc.
    - Elas são muito eficientes em termos de memória porque têm uma estrutura simples.
    - No entanto, elas podem ser menos legíveis porque você precisa lembrar o índice de cada elemento.

2.  **Dicionários**:
    - Dicionários usam pares chave-valor, o que permite que você acesse elementos por seus nomes.
    - Eles são mais legíveis, por exemplo, você pode usar `record['route']`, `record['date']`, etc.
    - Eles têm maior uso de memória devido à sobrecarga da tabela hash usada para armazenar os pares chave-valor.
    - Eles são flexíveis porque você pode adicionar ou remover campos facilmente.

3.  **Named Tuples**:
    - Named tuples combinam a eficiência das tuplas com a capacidade de acessar elementos por nome.
    - Você pode acessar elementos usando a notação de ponto, como `record.route`, `record.date`, etc.
    - Elas são imutáveis, assim como as tuplas regulares.
    - Elas são mais eficientes em termos de memória do que os dicionários.

4.  **Classes Regulares**:
    - Classes regulares seguem uma abordagem orientada a objetos e têm atributos nomeados.
    - Você pode acessar atributos usando a notação de ponto, como `record.route`, `record.date`, etc.
    - Você pode adicionar métodos a uma classe regular para definir o comportamento.
    - Elas usam mais memória porque cada instância tem um dicionário de instância para armazenar seus atributos.

5.  **Classes com \_\_slots\_\_**:
    - Classes com `__slots__` são classes otimizadas para memória. Elas evitam o uso de um dicionário de instância, o que economiza memória.
    - Elas ainda fornecem acesso nomeado aos atributos, como `record.route`, `record.date`, etc.
    - Elas restringem a adição de novos atributos após a criação do objeto.
    - Elas são mais eficientes em termos de memória do que as classes regulares.

## Quando Usar Cada Abordagem

- **Tuplas**: Use tuplas quando a memória for um fator crítico e você só precisar de acesso indexado simples aos seus dados.
- **Dicionários**: Use dicionários quando você precisar de flexibilidade, como quando os campos em seus dados podem variar.
- **Named Tuples**: Use named tuples quando você precisar de legibilidade e eficiência de memória.
- **Classes Regulares**: Use classes regulares quando você precisar adicionar comportamento (métodos) aos seus dados.
- **Classes com \_\_slots\_\_**: Use classes com `__slots__` quando você precisar de comportamento e máxima eficiência de memória.

Ao escolher a estrutura de dados certa para suas necessidades, você pode melhorar significativamente o desempenho e o uso de memória de seus programas Python, especialmente ao trabalhar com grandes conjuntos de dados.
