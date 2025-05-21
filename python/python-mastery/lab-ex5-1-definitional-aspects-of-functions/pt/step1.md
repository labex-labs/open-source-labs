# Compreendendo o Contexto

Em exercícios anteriores, você pode ter encontrado código que lê arquivos CSV e armazena os dados em várias estruturas de dados. O objetivo deste código é pegar dados de texto brutos de um arquivo CSV e convertê-los em objetos Python mais úteis, como dicionários ou instâncias de classe. Essa conversão é essencial porque nos permite trabalhar com os dados de uma forma mais estruturada e significativa dentro de nossos programas Python.

O padrão típico para leitura de arquivos CSV geralmente segue uma estrutura específica. Aqui está um exemplo de uma função que lê um arquivo CSV e converte cada linha em um dicionário:

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

Vamos detalhar como essa função funciona. Primeiro, ela importa o módulo `csv`, que fornece funcionalidade para trabalhar com arquivos CSV em Python. A função recebe dois parâmetros: `filename`, que é o nome do arquivo CSV a ser lido, e `types`, que é uma lista de funções usadas para converter os dados em cada coluna para o tipo de dados apropriado.

Dentro da função, ela inicializa uma lista vazia chamada `records` para armazenar os dicionários que representam cada linha do arquivo CSV. Em seguida, ela abre o arquivo usando a instrução `with`, que garante que o arquivo seja fechado corretamente após a execução do bloco de código. A função `csv.reader` é usada para criar um iterador que lê cada linha do arquivo CSV. A primeira linha é assumida como os cabeçalhos, então ela é recuperada usando a função `next`.

Em seguida, a função itera sobre as linhas restantes no arquivo CSV. Para cada linha, ela cria um dicionário usando uma compreensão de dicionário. As chaves do dicionário são os cabeçalhos das colunas, e os valores são o resultado da aplicação da função de conversão de tipo correspondente da lista `types` ao valor na linha. Finalmente, o dicionário é adicionado à lista `records`, e a função retorna a lista de dicionários.

Agora, vamos analisar uma função semelhante que lê dados de um arquivo CSV em instâncias de classe:

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Esta função é semelhante à anterior, mas em vez de criar dicionários, ela cria instâncias de uma classe. A função recebe dois parâmetros: `filename`, que é o nome do arquivo CSV a ser lido, e `cls`, que é a classe cujas instâncias serão criadas.

Dentro da função, ela segue uma estrutura semelhante à função anterior. Ela inicializa uma lista vazia chamada `records` para armazenar as instâncias da classe. Em seguida, ela abre o arquivo, lê os cabeçalhos e itera sobre as linhas restantes. Para cada linha, ela chama o método `from_row` da classe `cls` para criar uma instância da classe usando os dados da linha. A instância é então adicionada à lista `records`, e a função retorna a lista de instâncias.

Neste laboratório, vamos refatorar essas funções para torná-las mais flexíveis e robustas. Também exploraremos o sistema de _type hinting_ (anotação de tipo) do Python, que nos permite especificar os tipos esperados dos parâmetros e valores de retorno de nossas funções. Isso pode tornar nosso código mais legível e fácil de entender, especialmente para outros desenvolvedores que podem estar trabalhando com nosso código.

Vamos começar criando um arquivo `reader.py` e adicionando essas funções iniciais a ele. Certifique-se de testar essas funções para garantir que elas funcionem corretamente antes de prosseguir para as próximas etapas.
