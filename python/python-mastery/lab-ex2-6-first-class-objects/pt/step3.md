# Explorando o Modelo de Memória do Python

O modelo de memória do Python desempenha um papel crucial na determinação de como os objetos são armazenados na memória e como eles são referenciados. Compreender este modelo é essencial, especialmente ao lidar com grandes conjuntos de dados, pois pode impactar significativamente o desempenho e o uso de memória de seus programas Python. Nesta etapa, focaremos especificamente em como os objetos string são tratados em Python e exploraremos maneiras de otimizar o uso de memória para grandes conjuntos de dados.

## Repetição de Strings em Conjuntos de Dados

Os dados do ônibus CTA contêm muitos valores repetidos, como nomes de rotas. Valores repetidos em um conjunto de dados podem levar ao uso ineficiente de memória se não forem tratados corretamente. Para entender a extensão desse problema, vamos primeiro examinar quantos strings de rota exclusivos existem no conjunto de dados.

Primeiro, abra um interpretador Python. Você pode fazer isso executando o seguinte comando em seu terminal:

```bash
python3
```

Depois que o interpretador Python estiver aberto, carregaremos os dados do ônibus CTA e encontraremos as rotas exclusivas. Aqui está o código para conseguir isso:

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Encontre nomes de rotas exclusivos
routes = {row['route'] for row in rows}
print(f"Número de nomes de rotas exclusivos: {len(routes)}")
```

Neste código, primeiro importamos o módulo `reader`, que presumivelmente contém uma função para ler arquivos CSV como dicionários. Em seguida, usamos a função `read_csv_as_dicts` para carregar os dados do arquivo `ctabus.csv`. O segundo argumento `[str, str, str, int]` especifica os tipos de dados para cada coluna no arquivo CSV. Depois disso, usamos uma compreensão de conjunto para encontrar todos os nomes de rotas exclusivos no conjunto de dados e imprimir o número de nomes de rotas exclusivos.

A saída deve ser:

```
Número de nomes de rotas exclusivos: 181
```

Agora, vamos verificar quantos objetos string diferentes são criados para essas rotas. Embora existam apenas 181 nomes de rotas exclusivos, o Python pode criar um novo objeto string para cada ocorrência de um nome de rota no conjunto de dados. Para verificar isso, usaremos a função `id()` para obter o identificador exclusivo de cada objeto string.

```python
# Contar IDs de objetos string exclusivos
routeids = {id(row['route']) for row in rows}
print(f"Número de objetos string de rota exclusivos: {len(routeids)}")
```

A saída pode surpreendê-lo:

```
Número de objetos string de rota exclusivos: 542305
```

Isso mostra que existem apenas 181 nomes de rotas exclusivos, mas mais de 500.000 objetos string exclusivos. Isso acontece porque o Python cria um novo objeto string para cada linha, mesmo que os valores sejam os mesmos. Isso pode levar a um desperdício significativo de memória, especialmente ao lidar com grandes conjuntos de dados.

## String Interning para Economizar Memória

O Python fornece uma maneira de "internar" (reutilizar) strings usando a função `sys.intern()`. O string interning pode economizar memória quando você tem muitas strings duplicadas em seu conjunto de dados. Quando você interna uma string, o Python verifica se uma string idêntica já existe no pool de internamento. Se existir, ele retorna uma referência ao objeto string existente em vez de criar um novo.

Vamos demonstrar como o string interning funciona com um exemplo simples:

```python
import sys

# Sem interning
a = 'hello world'
b = 'hello world'
print(f"a é b (sem interning): {a is b}")

# Com interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a é b (com interning): {a is b}")
```

Neste código, primeiro criamos duas variáveis string `a` e `b` com o mesmo valor sem interning. O operador `is` verifica se duas variáveis se referem ao mesmo objeto. Sem interning, `a` e `b` são objetos diferentes, então `a is b` retorna `False`. Em seguida, internamos ambas as strings usando `sys.intern()`. Após o interning, `a` e `b` se referem ao mesmo objeto no pool de internamento, então `a is b` retorna `True`.

A saída deve ser:

```
a é b (sem interning): False
a é b (com interning): True
```

Agora, vamos usar o string interning ao ler os dados do ônibus CTA para reduzir o uso de memória. Também usaremos o módulo `tracemalloc` para rastrear o uso de memória antes e depois do interning.

```python
import sys
import reader
import tracemalloc

# Iniciar o rastreamento de memória
tracemalloc.start()

# Ler dados com interning para a coluna de rota
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Verificar objetos de rota exclusivos novamente
routeids = {id(row['route']) for row in rows}
print(f"Número de objetos string de rota exclusivos (com interning): {len(routeids)}")

# Verificar o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual: {current / 1024 / 1024:.2f} MB")
print(f"Uso de memória de pico: {peak / 1024 / 1024:.2f} MB")
```

Neste código, primeiro iniciamos o rastreamento de memória usando `tracemalloc.start()`. Em seguida, lemos os dados do ônibus CTA com interning para a coluna de rota, passando `sys.intern` como o tipo de dados para a primeira coluna. Depois disso, verificamos o número de objetos string de rota exclusivos novamente e imprimimos o uso de memória atual e de pico.

A saída deve ser algo como:

```
Número de objetos string de rota exclusivos (com interning): 181
Uso de memória atual: 189.56 MB
Uso de memória de pico: 209.32 MB
```

Vamos reiniciar o interpretador e tentar internar as strings de rota e data para ver se podemos reduzir ainda mais o uso de memória.

```python
exit()
```

Inicie o Python novamente:

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Iniciar o rastreamento de memória
tracemalloc.start()

# Ler dados com interning para as colunas de rota e data
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Verificar o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Uso de memória atual (interning rota e data): {current / 1024 / 1024:.2f} MB")
print(f"Uso de memória de pico (interning rota e data): {peak / 1024 / 1024:.2f} MB")
```

A saída deve mostrar uma diminuição adicional no uso de memória:

```
Uso de memória atual (interning rota e data): 170.23 MB
Uso de memória de pico (interning rota e data): 190.05 MB
```

Isso demonstra como a compreensão do modelo de memória do Python e o uso de técnicas como string interning podem ajudar a otimizar seus programas, especialmente ao lidar com grandes conjuntos de dados contendo valores repetidos.

Finalmente, saia do interpretador Python:

```python
exit()
```
