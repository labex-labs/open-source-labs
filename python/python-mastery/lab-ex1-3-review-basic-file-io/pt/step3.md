# Processando os Dados

Agora que aprendemos como ler um arquivo, a próxima etapa é processar cada linha do arquivo para calcular o custo de cada compra de ação. Esta é uma parte importante de trabalhar com dados em Python, pois nos permite extrair informações significativas do arquivo.

Cada linha no arquivo segue um formato específico: `[Símbolo da Ação] [Número de Ações] [Preço por Ação]`. Para calcular o custo de cada compra de ação, precisamos extrair o número de ações e o preço por ação de cada linha. Em seguida, multiplicamos esses dois valores para obter o custo daquela compra de ação específica. Finalmente, adicionamos esse custo ao nosso total acumulado para encontrar o custo geral do portfólio.

Vamos modificar a função `portfolio_cost()` no arquivo `pcost.py` para conseguir isso. Aqui está o código modificado:

```python
def portfolio_cost(filename):
    """
    Calcula o custo total (ações*preço) de um arquivo de portfólio
    """
    total_cost = 0.0

    # Abrir o arquivo
    with open(filename, 'r') as file:
        # Ler todas as linhas do arquivo
        for line in file:
            # Remover qualquer espaço em branco no início/fim
            line = line.strip()

            # Ignorar linhas vazias
            if not line:
                continue

            # Dividir a linha em campos
            fields = line.split()

            # Extrair os dados relevantes
            # fields[0] é o símbolo da ação (que não precisamos para o cálculo)
            shares = int(fields[1])  # Número de ações (segundo campo)
            price = float(fields[2])  # Preço por ação (terceiro campo)

            # Calcular o custo desta compra de ação
            cost = shares * price

            # Adicionar ao custo total
            total_cost += cost

            # Imprimir algumas informações de depuração
            print(f'{fields[0]}: {shares} ações a ${price:.2f} = ${cost:.2f}')

    # Retornar o custo total
    return total_cost
```

Vamos detalhar o que esta função modificada faz passo a passo:

1.  **Remove espaços em branco**: Usamos o método `strip()` para remover qualquer espaço em branco no início ou no final de cada linha. Isso garante que não incluamos acidentalmente espaços extras ao dividir a linha em campos.
2.  **Ignora linhas vazias**: Se uma linha estiver vazia (ou seja, contiver apenas espaços em branco), usamos a instrução `continue` para ignorá-la. Isso nos ajuda a evitar erros ao tentar dividir uma linha vazia.
3.  **Divide a linha em campos**: Usamos o método `split()` para dividir cada linha em uma lista de campos com base em espaços em branco. Isso nos permite acessar cada parte da linha separadamente.
4.  **Extrai dados relevantes**: Extraímos o número de ações e o preço por ação da lista de campos. O número de ações é o segundo campo, e o preço por ação é o terceiro campo. Convertemos esses valores para os tipos de dados apropriados (`int` para ações e `float` para preço) para que possamos realizar operações aritméticas neles.
5.  **Calcula o custo**: Multiplicamos o número de ações pelo preço por ação para calcular o custo desta compra de ação.
6.  **Adiciona ao total**: Adicionamos o custo desta compra de ação ao custo total acumulado.
7.  **Imprime informações de depuração**: Imprimimos algumas informações sobre cada compra de ação para nos ajudar a ver o que está acontecendo. Isso inclui o símbolo da ação, o número de ações, o preço por ação e o custo total da compra.

Agora, vamos executar o código para ver se ele funciona. Abra seu terminal e execute o seguinte comando:

```bash
python3 ~/project/pcost.py
```

Após executar o comando, você deve ver informações detalhadas sobre cada compra de ação, seguido pelo custo total do portfólio. Esta saída ajudará você a verificar se a função está funcionando corretamente e se você calculou o custo total com precisão.
