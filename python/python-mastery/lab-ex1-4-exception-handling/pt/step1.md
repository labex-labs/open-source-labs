# Definindo uma Função

Nesta etapa, vamos aprender como criar uma função. Uma função em Python é um bloco de código organizado e reutilizável que é usado para executar uma única ação relacionada. Aqui, nossa função lerá dados de portfólio de um arquivo e calculará o custo total. Isso é útil porque, uma vez que temos essa função, podemos usá-la várias vezes com diferentes arquivos de portfólio, evitando escrever o mesmo código repetidamente.

## Entendendo o Problema

No laboratório anterior, você pode ter escrito algum código para ler dados de portfólio e calcular o custo total. Mas esse código provavelmente foi escrito de uma forma que não pode ser facilmente reutilizada. Agora, vamos converter esse código em uma função reutilizável.

Os arquivos de dados do portfólio têm um formato específico. Eles contêm informações na forma de "Símbolo Ações Preço". Cada linha no arquivo representa uma participação acionária. Por exemplo, em um arquivo chamado `portfolio.dat`, você pode ver linhas como esta:

```
AA 100 32.20
IBM 50 91.10
...
```

Aqui, a primeira parte (como "AA" ou "IBM") é o símbolo da ação, que é um identificador único para a ação. A segunda parte é o número de ações que você possui dessa ação, e a terceira parte é o preço por ação.

## Criando a Função

Vamos criar um arquivo Python chamado `pcost.py` no diretório `/home/labex/project`. Este arquivo conterá nossa função. Aqui está o código que colocaremos no arquivo `pcost.py`:

```python
def portfolio_cost(filename):
    """
    Computa o custo total (ações*preço) de um arquivo de portfólio

    Args:
        filename: O nome do arquivo de portfólio

    Returns:
        O custo total do portfólio como um float
    """
    total_cost = 0.0

    # Abre o arquivo e lê cada linha
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extrai os dados (símbolo, ações, preço)
            shares = int(fields[1])
            price = float(fields[2])
            # Adiciona o custo ao nosso total acumulado
            total_cost += shares * price

    return total_cost

# Chama a função com o arquivo portfolio.dat
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

Neste código, primeiro definimos uma função chamada `portfolio_cost` que recebe um `filename` como argumento. Dentro da função, inicializamos uma variável `total_cost` para 0.0. Em seguida, abrimos o arquivo usando a função `open` no modo de leitura (`'r'`). Usamos um loop `for` para percorrer cada linha do arquivo. Para cada linha, dividimos em campos usando o método `split()`. Em seguida, extraímos o número de ações e o convertemos em um inteiro, e o preço e o convertemos em um float. Calculamos o custo para essa participação acionária multiplicando o número de ações pelo preço e adicionando-o ao `total_cost`. Finalmente, retornamos o `total_cost`.

A parte `if __name__ == '__main__':` é usada para chamar a função quando o script é executado diretamente. Passamos o caminho para o arquivo `portfolio.dat` para a função e imprimimos o resultado.

## Testando a Função

Agora, vamos executar o programa para ver se ele funciona. Precisamos navegar até o diretório onde o arquivo `pcost.py` está localizado e, em seguida, executar o script Python. Aqui estão os comandos para fazer isso:

```bash
cd /home/labex/project
python3 pcost.py
```

Após executar esses comandos, você deverá ver a saída:

```
44671.15
```

Essa saída representa o custo total de todas as ações no portfólio.

## Entendendo o Código

Vamos detalhar o que nossa função faz passo a passo:

1.  Ele recebe um `filename` como um parâmetro de entrada. Isso nos permite usar a função com diferentes arquivos de portfólio.
2.  Ele abre o arquivo e o lê linha por linha. Isso é feito usando a função `open` e um loop `for`.
3.  Para cada linha, ele divide a linha em campos usando o método `split()`. Este método divide a linha em uma lista de strings com base em espaços em branco.
4.  Ele converte o número de ações em um inteiro e o preço em um float. Isso é necessário porque os dados lidos do arquivo estão em formato de string, e precisamos realizar operações aritméticas neles.
5.  Ele calcula o custo (ações \* preço) para cada participação acionária e o adiciona ao total acumulado. Isso nos dá o custo total do portfólio.
6.  Ele retorna o custo total final. Isso nos permite usar o resultado em outras partes do nosso programa, se necessário.

Esta função agora é reutilizável. Podemos chamá-la com diferentes arquivos de portfólio para calcular seus custos, o que torna nosso código mais eficiente e fácil de manter.
