# Medindo o Uso de Memória com Diferentes Métodos de Armazenamento

Nesta etapa, vamos analisar como diferentes formas de armazenar dados podem impactar o uso de memória. O uso de memória é um aspecto importante da programação, especialmente ao lidar com grandes conjuntos de dados. Para medir a memória usada pelo nosso código Python, usaremos o módulo `tracemalloc` do Python. Este módulo é muito útil, pois nos permite rastrear as alocações de memória feitas pelo Python. Ao usá-lo, podemos ver quanta memória nossos métodos de armazenamento de dados estão consumindo.

## Método 1: Armazenando o Arquivo Inteiro como uma Única String

Vamos começar criando um novo arquivo Python. Navegue até o diretório `/home/labex/project` e crie um arquivo chamado `memory_test1.py`. Você pode usar um editor de texto para abrir este arquivo. Depois que o arquivo estiver aberto, adicione o seguinte código a ele. Este código lerá todo o conteúdo de um arquivo como uma única string e medirá o uso de memória.

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

Depois de adicionar o código, salve o arquivo. Agora, para executar este script, abra seu terminal e execute o seguinte comando:

```bash
python3 /home/labex/project/memory_test1.py
```

Ao executar o script, você deve ver uma saída semelhante a esta:

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

Os números exatos podem ser diferentes em seu sistema, mas, em geral, você notará que o uso atual de memória é de cerca de 12 MB e o uso máximo de memória é de cerca de 24 MB.

## Método 2: Armazenando como uma Lista de Strings

Em seguida, testaremos outra forma de armazenar os dados. Crie um novo arquivo chamado `memory_test2.py` no mesmo diretório `/home/labex/project`. Abra este arquivo no editor e adicione o seguinte código. Este código lê o arquivo e armazena cada linha como uma string separada em uma lista e, em seguida, mede o uso de memória.

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

Salve o arquivo e, em seguida, execute o script usando o seguinte comando no terminal:

```bash
python3 /home/labex/project/memory_test2.py
```

Você deve ver uma saída semelhante a esta:

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Observe que o uso de memória aumentou significativamente em comparação com o método anterior de armazenar os dados como uma única string. Isso ocorre porque cada linha na lista é um objeto string Python separado, e cada objeto tem sua própria sobrecarga de memória.

## Compreendendo a Diferença de Memória

A diferença no uso de memória entre as duas abordagens mostra um conceito importante na programação Python chamado sobrecarga de objeto (object overhead). Quando você armazena dados como uma lista de strings, cada string é um objeto Python separado. Cada objeto tem alguns requisitos de memória adicionais, que incluem:

1.  O cabeçalho do objeto Python (geralmente 16 a 24 bytes por objeto). Este cabeçalho contém informações sobre o objeto, como seu tipo e contagem de referência.
2.  A própria representação real da string, que armazena os caracteres da string.
3.  Preenchimento de alinhamento de memória. Este é um espaço extra adicionado para garantir que o endereço de memória do objeto seja devidamente alinhado para acesso eficiente.

Por outro lado, quando você armazena todo o conteúdo do arquivo como uma única string, há apenas um objeto e, portanto, apenas um conjunto de sobrecarga. Isso o torna mais eficiente em termos de memória ao considerar o tamanho total dos dados.

Ao projetar programas que funcionam com grandes conjuntos de dados, você precisa considerar essa compensação (trade-off) entre eficiência de memória e acessibilidade de dados. Às vezes, pode ser mais conveniente acessar dados quando eles são armazenados em uma lista de strings, mas isso usará mais memória. Em outros momentos, você pode priorizar a eficiência da memória e optar por armazenar os dados como uma única string.
