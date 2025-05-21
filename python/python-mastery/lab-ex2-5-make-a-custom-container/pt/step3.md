# Otimizando a Memória com Dados Orientados a Colunas

No armazenamento de dados tradicional, frequentemente armazenamos cada registro como um dicionário separado, o que é chamado de abordagem orientada a linhas. No entanto, esse método pode consumir uma quantidade significativa de memória. Uma forma alternativa é armazenar dados em colunas. Na abordagem orientada a colunas, criamos listas separadas para cada atributo, e cada lista contém todos os valores para aquele atributo específico. Isso pode nos ajudar a economizar memória.

1. Primeiro, você precisa criar um novo arquivo Python no diretório do seu projeto. Este arquivo conterá o código para ler dados de forma orientada a colunas. Nomeie o arquivo `readrides.py`. Você pode usar os seguintes comandos no terminal para fazer isso:

```bash
cd ~/project
touch readrides.py
```

O comando `cd ~/project` altera o diretório atual para o seu diretório de projeto, e o comando `touch readrides.py` cria um novo arquivo vazio chamado `readrides.py`.

2. Em seguida, abra o arquivo `readrides.py` no editor WebIDE. Depois, adicione o seguinte código Python ao arquivo. Este código define uma função `read_rides_as_columns` que lê dados de viagens de ônibus de um arquivo CSV e os armazena em quatro listas separadas, cada uma representando uma coluna de dados.

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

Neste código, primeiro importamos os módulos necessários `csv`, `sys` e `tracemalloc`. O módulo `csv` é usado para ler arquivos CSV, `sys` pode ser usado para operações relacionadas ao sistema (embora não seja usado nesta função), e `tracemalloc` é usado para perfilamento de memória. Dentro da função, inicializamos quatro listas vazias para armazenar diferentes colunas de dados. Em seguida, abrimos o arquivo, ignoramos a linha de cabeçalho e iteramos por cada linha no arquivo, adicionando os valores correspondentes às listas apropriadas. Finalmente, retornamos um dicionário contendo essas quatro listas.

3. Agora, vamos analisar por que a abordagem orientada a colunas pode economizar memória. Faremos isso no shell Python. Execute o seguinte código:

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

Neste código, primeiro importamos o módulo `readrides` que acabamos de criar e o módulo `tracemalloc`. Em seguida, estimamos o uso de memória para a abordagem orientada a linhas. Assumimos que cada dicionário tem uma sobrecarga (overhead) de 240 bytes, e multiplicamos isso pelo número de linhas no arquivo original para obter o uso total de memória para os dados orientados a linhas. Para a abordagem orientada a colunas, assumimos que em um sistema de 64 bits, cada ponteiro (pointer) ocupa 8 bytes. Como temos 4 colunas e um ponteiro por entrada, calculamos o uso total de memória para os dados orientados a colunas. Finalmente, calculamos a economia de memória subtraindo o uso de memória orientado a colunas do uso de memória orientado a linhas.

Este cálculo mostra que a abordagem orientada a colunas deve economizar cerca de 120MB de memória em comparação com a abordagem orientada a linhas com dicionários.

4. Vamos verificar isso medindo o uso real de memória com o módulo `tracemalloc`. Execute o seguinte código:

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

Neste código, primeiro começamos a rastrear a memória usando `tracemalloc.start()`. Em seguida, chamamos a função `read_rides_as_columns` para ler os dados do arquivo `ctabus.csv`. Depois disso, usamos `tracemalloc.get_traced_memory()` para obter o uso atual e de pico de memória. Finalmente, paramos de rastrear a memória usando `tracemalloc.stop()`.

A saída mostrará o uso real de memória da sua estrutura de dados orientada a colunas. Isso deve ser significativamente menor do que nossa estimativa teórica para a abordagem orientada a linhas.

A economia significativa de memória vem da eliminação da sobrecarga de milhares de objetos de dicionário. Cada dicionário em Python tem uma sobrecarga fixa, independentemente de quantos itens ele contém. Ao usar o armazenamento orientado a colunas, precisamos apenas de algumas listas em vez de milhares de dicionários.
