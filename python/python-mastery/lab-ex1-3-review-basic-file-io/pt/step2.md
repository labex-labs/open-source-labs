# Abrindo e Lendo o Arquivo

Nesta etapa, vamos aprender como abrir e ler um arquivo em Python. A entrada/saída de arquivos (I/O) é um conceito fundamental em programação. Ele permite que seu programa interaja com arquivos externos, como arquivos de texto, arquivos CSV e muito mais. Em Python, uma das maneiras mais comuns de trabalhar com arquivos é usando a função `open()`.

A função `open()` é usada para abrir um arquivo em Python. Ela recebe dois argumentos importantes. O primeiro argumento é o nome do arquivo que você deseja abrir. O segundo argumento é o modo no qual você deseja abrir o arquivo. Quando você deseja ler um arquivo, você usa o modo 'r'. Isso informa ao Python que você só deseja ler o conteúdo do arquivo e não fazer nenhuma alteração nele.

Agora, vamos adicionar algum código ao arquivo `pcost.py` para abrir e ler o arquivo `portfolio.dat`. Abra o arquivo `pcost.py` no seu editor de código e adicione o seguinte código:

```python
# pcost.py
# Calcular o custo total de um portfólio de ações

def portfolio_cost(filename):
    """
    Calcula o custo total (ações*preço) de um arquivo de portfólio
    """
    total_cost = 0.0

    # Abrir o arquivo
    with open(filename, 'r') as file:
        # Ler todas as linhas do arquivo
        for line in file:
            print(line)  # Apenas para depuração, para ver o que estamos lendo

    # Retornar o custo total
    return total_cost

# Chamar a função com o arquivo do portfólio
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

Vamos detalhar o que este código faz:

1. Primeiro, definimos uma função chamada `portfolio_cost()`. Esta função recebe um nome de arquivo como um parâmetro de entrada. O objetivo desta função é calcular o custo total de um portfólio de ações com base nos dados do arquivo.
2. Dentro da função, usamos a função `open()` para abrir o arquivo especificado no modo de leitura. A instrução `with` é usada aqui para garantir que o arquivo seja fechado corretamente depois de terminarmos de lê-lo. Esta é uma boa prática para evitar vazamentos de recursos.
3. Em seguida, usamos um loop `for` para ler o arquivo linha por linha. Para cada linha no arquivo, imprimimos. Isso é apenas para fins de depuração, para que possamos ver quais dados estamos lendo do arquivo.
4. Depois de ler o arquivo, a função retorna o custo total. Atualmente, o custo total é definido como 0.0 porque ainda não implementamos o cálculo real.
5. Fora da função, chamamos a função `portfolio_cost()` com o nome do arquivo 'portfolio.dat'. Isso significa que estamos pedindo à função para calcular o custo total com base nos dados do arquivo `portfolio.dat`.
6. Finalmente, imprimimos o custo total usando uma f-string.

Agora, vamos executar este código para ver o que ele faz. Você pode executar o arquivo Python do terminal usando o seguinte comando:

```bash
python3 ~/project/pcost.py
```

Quando você executa este comando, você deve ver cada linha do arquivo `portfolio.dat` impressa no terminal, seguida pelo custo total, que atualmente está definido como 0.0. Esta saída ajuda você a verificar se o arquivo está sendo lido corretamente.
