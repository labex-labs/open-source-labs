# Finalizando o Programa

Agora, vamos limpar nosso código e criar a versão final do programa `pcost.py`. Limpar o código significa remover quaisquer partes desnecessárias e garantir que a saída tenha uma boa aparência. Esta é uma etapa importante na programação porque torna nosso código mais profissional e mais fácil de entender.

Começaremos removendo as instruções de impressão de depuração. Essas instruções são usadas durante o desenvolvimento para verificar os valores das variáveis e o fluxo do programa, mas não são necessárias na versão final. Em seguida, garantiremos que a saída final seja formatada de forma agradável.

Aqui está a versão final do código `pcost.py`:

```python
# pcost.py
# Calcular o custo total de um portfólio de ações

def portfolio_cost(filename):
    """
    Calcula o custo total (ações*preço) de um arquivo de portfólio
    """
    total_cost = 0.0

    try:
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

                # Calcular o custo desta compra de ação e adicionar ao total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Retornar o custo total
    return total_cost

# Bloco principal para executar quando o script é executado diretamente
if __name__ == '__main__':
    # Chamar a função com o arquivo do portfólio
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

Esta versão final do código tem várias melhorias:

1.  Tratamento de erros: Adicionamos código para capturar dois tipos de erros. O `FileNotFoundError` é gerado quando o arquivo especificado não existe. Se isso acontecer, o programa imprimirá uma mensagem de erro e retornará 0.0. O bloco `Exception` captura quaisquer outros erros que possam ocorrer durante o processamento do arquivo. Isso torna nosso programa mais robusto e menos propenso a travar inesperadamente.
2.  Formatação adequada: O custo total é formatado para duas casas decimais usando o especificador de formato `: .2f` na f-string. Isso faz com que a saída pareça mais profissional e mais fácil de ler.
3.  Verificação `__name__ == '__main__'`: Este é um idioma Python comum. Ele garante que o código dentro do bloco `if` seja executado apenas quando o script for executado diretamente. Se o script for importado como um módulo em outro script, este código não será executado. Isso nos dá mais controle sobre como nosso script se comporta.

Agora, vamos executar o código final. Abra seu terminal e digite o seguinte comando:

```bash
python3 ~/project/pcost.py
```

Quando você executar este comando, o programa lerá o arquivo `portfolio.dat`, calculará o custo total do portfólio e imprimirá o resultado. Você deve ver o custo total do portfólio, que deve ser $44671.15.

Parabéns! Você criou com sucesso um programa Python que lê dados de um arquivo, os processa e calcula um resultado. Esta é uma grande conquista e mostra que você está a caminho de se tornar um programador Python proficiente.
