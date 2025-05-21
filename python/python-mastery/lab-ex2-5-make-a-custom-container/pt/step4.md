# Criando uma Classe Contêiner Personalizada

No processamento de dados, a abordagem orientada a colunas é ótima para economizar memória. No entanto, ela pode causar problemas quando seu código existente espera que os dados estejam na forma de uma lista de dicionários. Para resolver esse problema, criaremos uma classe contêiner personalizada. Essa classe apresentará uma interface orientada a linhas, o que significa que ela se parecerá e agirá como uma lista de dicionários para o seu código. Mas internamente, ela armazenará os dados em um formato orientado a colunas, ajudando-nos a economizar memória.

1. Primeiro, abra o arquivo `readrides.py` no editor WebIDE. Vamos adicionar uma nova classe a este arquivo. Essa classe será a base do nosso contêiner personalizado.

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

Neste código, definimos uma classe chamada `RideData` que herda de `Sequence`. O método `__init__` inicializa quatro listas vazias, cada uma representando uma coluna de dados. O método `__len__` retorna o comprimento do contêiner, que é o mesmo que o comprimento da lista `routes`. O método `__getitem__` nos permite acessar um registro específico por índice, retornando-o como um dicionário. O método `append` adiciona um novo registro ao contêiner, adicionando valores a cada lista de coluna.

2. Agora, precisamos de uma função para ler os dados de viagens de ônibus em nosso contêiner personalizado. Adicione a seguinte função ao arquivo `readrides.py`.

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

Esta função cria uma instância da classe `RideData` e a preenche com dados do arquivo CSV. Ela lê cada linha do arquivo, extrai as informações relevantes, cria um dicionário para cada registro e, em seguida, o adiciona ao contêiner `RideData`. O ponto-chave é que ela mantém a mesma interface que uma lista de dicionários, mas internamente armazena os dados em colunas.

3. Vamos testar nosso contêiner personalizado no shell Python. Isso nos ajudará a verificar se ele funciona como esperado.

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

Nosso contêiner personalizado implementa com sucesso a interface `Sequence`, o que significa que ele se comporta como uma lista. Você pode usar a função `len()` para obter o número de registros no contêiner e pode usar a indexação para acessar registros individuais. Cada registro parece ser um dicionário, embora os dados sejam armazenados em colunas internamente. Isso é ótimo porque o código existente que espera uma lista de dicionários continuará a funcionar com nosso contêiner personalizado sem qualquer modificação.

4. Finalmente, vamos medir o uso de memória do nosso contêiner personalizado. Isso nos mostrará quanta memória estamos economizando em comparação com uma lista de dicionários.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

Quando você executa este código, você deve ver que o uso de memória é semelhante à abordagem orientada a colunas, que é muito menor do que o que uma lista de dicionários usaria. Isso demonstra a vantagem do nosso contêiner personalizado em termos de eficiência de memória.
