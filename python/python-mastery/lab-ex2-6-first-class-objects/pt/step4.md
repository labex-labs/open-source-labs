# Armazenamento de Dados Orientado a Colunas

Até agora, temos armazenado dados CSV como uma lista de dicionários de linhas. Isso significa que cada linha no arquivo CSV é representada como um dicionário, onde as chaves são os cabeçalhos das colunas e os valores são os dados correspondentes nessa linha. No entanto, ao lidar com grandes conjuntos de dados, esse método pode ser ineficiente. Armazenar dados em um formato orientado a colunas pode ser uma escolha melhor. Em uma abordagem orientada a colunas, os dados de cada coluna são armazenados em uma lista separada. Isso pode reduzir significativamente o uso de memória porque tipos de dados semelhantes são agrupados e também pode melhorar o desempenho para certas operações, como agregar dados por coluna.

## Criando um Leitor de Dados Orientado a Colunas

Agora, vamos criar um novo arquivo que nos ajudará a ler dados CSV em um formato orientado a colunas. Crie um novo arquivo chamado `colreader.py` no diretório do projeto com o seguinte código:

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Inicializa uma coleção de dados orientada a colunas.

        Parâmetros:
        headers (list): Nomes dos cabeçalhos das colunas
        columns (dict): Dicionário mapeando nomes de cabeçalhos para listas de dados de colunas
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Retorna o número de linhas na coleção."""
        return self._length

    def __getitem__(self, index):
        """
        Obtém uma linha por índice, apresentada como um dicionário.

        Parâmetros:
        index (int): Índice da linha

        Retorna:
        dict: Dicionário representando a linha no índice fornecido
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Índice fora do intervalo")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Índice deve ser um inteiro")

def read_csv_as_columns(filename, types):
    """
    Lê um arquivo CSV em uma estrutura de dados orientada a colunas, convertendo cada campo
    de acordo com os tipos fornecidos.

    Parâmetros:
    filename (str): Nome do arquivo CSV a ser lido
    types (list): Lista de funções de conversão de tipo para cada coluna

    Retorna:
    DataCollection: Coleção de dados orientada a colunas representando os dados CSV
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Obtenha os cabeçalhos das colunas

        # Inicialize as colunas
        columns = {header: [] for header in headers}

        # Leia os dados nas colunas
        for row in rows:
            # Converta os valores de acordo com os tipos especificados
            converted_values = [func(val) for func, val in zip(types, row)]

            # Adicione cada valor à sua coluna correspondente
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

Este código faz duas coisas importantes:

1.  Ele define uma classe `DataCollection`. Esta classe armazena dados em colunas, mas nos permite acessar os dados como se fossem uma lista de dicionários de linhas. Isso é útil porque fornece uma maneira familiar de trabalhar com os dados.
2.  Ele define uma função `read_csv_as_columns`. Esta função lê dados CSV de um arquivo e os armazena em uma estrutura orientada a colunas. Ele também converte cada campo no arquivo CSV de acordo com os tipos que fornecemos.

## Testando o Leitor Orientado a Colunas

Vamos testar nosso leitor orientado a colunas usando os dados do ônibus CTA. Primeiro, abra um interpretador Python. Você pode fazer isso executando o seguinte comando em seu terminal:

```bash
python3
```

Depois que o interpretador Python estiver aberto, execute o seguinte código:

```python
import colreader
import tracemalloc
from sys import intern

# Iniciar o rastreamento de memória
tracemalloc.start()

# Ler dados em estrutura orientada a colunas com string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Verifique se podemos acessar os dados como uma lista de dicionários
print(f"Número de linhas: {len(data)}")
print("Primeiras 3 linhas:")
for i in range(3):
    print(data[i])

# Verificar o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual: {current / 1024 / 1024:.2f} MB")
print(f"Uso de memória de pico: {peak / 1024 / 1024:.2f} MB")
```

A saída deve ser semelhante a esta:

```
Número de linhas: 577563
Primeiras 3 linhas:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Uso de memória atual: 38.67 MB
Uso de memória de pico: 103.42 MB
```

Agora, vamos comparar isso com nossa abordagem anterior orientada a linhas. Execute o seguinte código no mesmo interpretador Python:

```python
import reader
import tracemalloc
from sys import intern

# Redefinir o rastreamento de memória
tracemalloc.reset_peak()

# Ler dados em estrutura orientada a linhas com string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Verificar o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual (orientado a linhas): {current / 1024 / 1024:.2f} MB")
print(f"Uso de memória de pico (orientado a linhas): {peak / 1024 / 1024:.2f} MB")
```

A saída deve ser algo como:

```
Uso de memória atual (orientado a linhas): 170.23 MB
Uso de memória de pico (orientado a linhas): 190.05 MB
```

Como você pode ver, a abordagem orientada a colunas usa significativamente menos memória!

Vamos também testar se ainda podemos analisar os dados como antes. Execute o seguinte código:

```python
# Encontrar todas as rotas exclusivas nos dados orientados a colunas
routes = {row['route'] for row in data}
print(f"Número de rotas exclusivas: {len(routes)}")

# Contar viagens por rota (primeiros 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Mostrar as 5 principais rotas por total de viagens
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("5 principais rotas por total de viagens:")
for route, rides in top_routes:
    print(f"Rota {route}: {rides:,} viagens")
```

A saída deve ser:

```
Número de rotas exclusivas: 181
5 principais rotas por total de viagens:
Rota 9: 158,545,826 viagens
Rota 49: 129,872,910 viagens
Rota 77: 120,086,065 viagens
Rota 79: 109,348,708 viagens
Rota 4: 91,405,538 viagens
```

Finalmente, saia do interpretador Python executando o seguinte comando:

```python
exit()
```

Podemos ver que a abordagem orientada a colunas não apenas economiza memória, mas também nos permite realizar as mesmas análises de antes. Isso mostra como diferentes estratégias de armazenamento de dados podem ter um impacto significativo no desempenho, mantendo a mesma interface para trabalharmos com os dados.
