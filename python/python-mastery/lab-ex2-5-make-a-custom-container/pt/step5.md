# Aprimorando o Contêiner Personalizado para Fatiamento

Nosso contêiner personalizado é ótimo para acessar registros individuais. No entanto, há um problema quando se trata de fatiamento (slicing). Quando você tenta obter uma fatia do nosso contêiner, o resultado não é o que você normalmente esperaria.

Vamos entender por que isso acontece. Em Python, o fatiamento é uma operação comum usada para extrair uma parte de uma sequência. Mas para nosso contêiner personalizado, o Python não sabe como criar um novo objeto `RideData` com apenas os dados fatiados. Em vez disso, ele cria uma lista contendo os resultados da chamada `__getitem__` para cada índice na fatia.

1. Vamos testar o fatiamento no shell Python:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

Neste código, primeiro importamos o módulo `readrides`. Em seguida, lemos os dados do arquivo `ctabus.csv` em uma variável `rows`. Quando tentamos obter uma fatia dos primeiros 10 registros e verificar o tipo do resultado, descobrimos que é uma lista em vez de um objeto `RideData`. Imprimir o resultado pode mostrar algo inesperado, como uma lista de números em vez de dicionários.

2. Vamos modificar nossa classe `RideData` para lidar com o fatiamento corretamente. Abra `readrides.py` e atualize o método `__getitem__`:

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

Neste método `__getitem__` atualizado, primeiro verificamos se o `index` é uma fatia. Se for, criamos um novo objeto `RideData` chamado `result`. Em seguida, preenchemos este novo objeto com fatias das colunas de dados originais (`routes`, `dates`, `daytypes` e `numrides`). Isso garante que, quando fatiamos nosso contêiner personalizado, obtemos outro objeto `RideData` em vez de uma lista. Se o `index` não for uma fatia (ou seja, é um único índice), retornamos um dicionário contendo o registro relevante.

3. Vamos testar nossa capacidade de fatiamento aprimorada:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

Depois de atualizar o método `__getitem__`, podemos testar o fatiamento novamente. Quando obtemos uma fatia dos primeiros 10 registros, o tipo do resultado agora deve ser `readrides.RideData`. O comprimento da fatia deve ser 10, e acessar elementos individuais na fatia deve nos dar os mesmos resultados que acessar os elementos correspondentes no contêiner original.

4. Você também pode testar com diferentes padrões de fatia:

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

Aqui, estamos testando diferentes padrões de fatia. A primeira fatia `rows[0:20:2]` obtém todos os outros registros dos primeiros 20 registros, e o comprimento da fatia resultante deve ser 10. A segunda fatia `rows[-10:]` obtém os últimos 10 registros, e seu comprimento também deve ser 10.

Ao implementar corretamente o fatiamento, nosso contêiner personalizado agora se comporta ainda mais como uma lista Python padrão, mantendo a eficiência de memória do armazenamento orientado a colunas.

Essa abordagem de criar classes de contêiner personalizadas que imitam contêineres Python embutidos, mas com diferentes representações internas, é uma técnica poderosa para otimizar o uso de memória sem alterar a interface que seu código apresenta aos usuários.
