# Trabalhando com Dados Estruturados usando Tuplas

Até agora, temos lidado com o armazenamento de dados de texto bruto. Mas quando se trata de análise de dados, geralmente precisamos transformar os dados em formatos mais organizados e estruturados. Isso facilita a execução de várias operações e a obtenção de insights dos dados. Nesta etapa, aprenderemos como ler dados como uma lista de tuplas usando o módulo `csv`. Tuplas são uma estrutura de dados simples e útil em Python que pode conter vários valores.

## Criando uma Função de Leitura com Tuplas

Vamos criar um novo arquivo chamado `readrides.py` no diretório `/home/labex/project`. Este arquivo conterá o código para ler os dados de um arquivo CSV e armazená-los como uma lista de tuplas.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

Este script define uma função chamada `read_rides_as_tuples`. Veja o que ela faz passo a passo:

1.  Ele abre o arquivo CSV especificado pelo parâmetro `filename`. Isso nos permite acessar os dados dentro do arquivo.
2.  Ele usa o módulo `csv` para analisar cada linha do arquivo. A função `csv.reader` nos ajuda a dividir as linhas em valores individuais.
3.  Ele extrai os quatro campos (rota, data, tipo de dia e número de viagens) de cada linha. Esses campos são importantes para nossa análise de dados.
4.  Ele converte o campo 'rides' em um inteiro. Isso é necessário porque os dados no arquivo CSV estão inicialmente em formato de string, e precisamos de um valor numérico para cálculos.
5.  Ele cria uma tupla com esses quatro valores. Tuplas são imutáveis, o que significa que seus valores não podem ser alterados depois de criados.
6.  Ele adiciona a tupla a uma lista chamada `records`. Esta lista conterá todos os registros do arquivo CSV.

Agora, vamos executar o script. Abra seu terminal e digite o seguinte comando:

```bash
python3 /home/labex/project/readrides.py
```

Você deve ver uma saída semelhante a esta:

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Observe que o uso de memória aumentou em comparação com nossos exemplos anteriores. Existem algumas razões para isso:

1.  Agora estamos armazenando os dados em um formato estruturado (tuplas). Dados estruturados geralmente exigem mais memória porque têm uma organização definida.
2.  Cada valor na tupla é um objeto Python separado. Objetos Python têm alguma sobrecarga, o que contribui para o aumento do uso de memória.
3.  Temos uma estrutura de lista adicional que contém todas essas tuplas. Listas também ocupam memória para armazenar seus elementos.

A vantagem de usar essa abordagem é que nossos dados agora estão devidamente estruturados e prontos para análise. Podemos acessar facilmente campos específicos de cada registro por índice. Por exemplo:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

No entanto, acessar dados por índice numérico nem sempre é intuitivo. Pode ser difícil lembrar qual índice corresponde a qual campo, especialmente ao lidar com um grande número de campos. Na próxima etapa, exploraremos outras estruturas de dados que podem tornar nosso código mais legível e sustentável.
