# Retornando Múltiplos Valores de Funções

Em Python, quando você precisa que uma função retorne mais de um valor, existe uma solução prática: retornar uma tupla. Uma tupla é um tipo de estrutura de dados em Python. É uma sequência imutável, o que significa que, uma vez criada uma tupla, você não pode alterar seus elementos. Tuplas são úteis porque podem conter múltiplos valores de diferentes tipos, todos em um só lugar.

Vamos criar uma função para analisar linhas de configuração no formato `nome=valor`. O objetivo desta função é receber uma linha nesse formato e retornar tanto o nome quanto o valor como itens separados.

1.  Primeiro, você precisa criar um novo arquivo Python. Este arquivo conterá o código para nossa função e o código de teste. No diretório do projeto, crie um arquivo chamado `return_values.py`. Você pode usar o seguinte comando no terminal para criar este arquivo:

```
touch ~/project/return_values.py
```

2.  Agora, abra o arquivo `return_values.py` em seu editor de código. Dentro deste arquivo, escreveremos a função `parse_line`. Esta função recebe uma linha como entrada, a divide no primeiro sinal '=', e retorna o nome e o valor como uma tupla.

```python
def parse_line(line):
    """
    Analisa uma linha no formato 'nome=valor' e retorna tanto o nome quanto o valor.

    Args:
        line (str): Linha de entrada para analisar no formato 'nome=valor'

    Returns:
        tuple: Uma tupla contendo (nome, valor)
    """
    parts = line.split('=', 1)  # Divide no primeiro sinal de igual
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Retorna como uma tupla
```

Nesta função, o método `split` é usado para dividir a linha de entrada em duas partes no primeiro sinal '='. Se a linha estiver no formato `nome=valor` correto, extraímos o nome e o valor e os retornamos como uma tupla.

3.  Após definir a função, precisamos adicionar algum código de teste para ver se a função funciona como esperado. O código de teste chamará a função `parse_line` com uma entrada de amostra e imprimirá os resultados.

```python
# Teste a função parse_line
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Desempacotando a tupla em variáveis separadas
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

No código de teste, primeiro chamamos a função `parse_line` e armazenamos a tupla retornada na variável `result`. Em seguida, imprimimos esta tupla. Depois, usamos o desempacotamento de tupla para atribuir diretamente os elementos da tupla às variáveis `name` e `value` e imprimimos-os separadamente.

4.  Depois de escrever a função e o código de teste, salve o arquivo `return_values.py`. Em seguida, abra o terminal e execute o seguinte comando para executar o script Python:

```
python ~/project/return_values.py
```

Você deve ver uma saída semelhante a:

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Explicação:**

- A função `parse_line` divide a string de entrada no caractere '=' usando o método `split`. Este método divide a string em partes com base no separador especificado.
- Ela retorna ambas as partes como uma tupla usando a sintaxe `return (name, value)`. Uma tupla é uma maneira de agrupar múltiplos valores juntos.
- Ao chamar a função, você tem duas opções. Você pode armazenar toda a tupla em uma variável, como fizemos com a variável `result`. Ou você pode "desempacotar" a tupla diretamente em variáveis separadas usando a sintaxe `name, value = parse_line(...)`. Isso facilita o trabalho com os valores individuais.

Este padrão de retornar múltiplos valores como uma tupla é muito comum em Python. Ele torna as funções mais versáteis porque elas podem fornecer mais de uma informação ao código que as chama.
