# Aprimorando o Pipeline de Corrotina

Agora que temos um pipeline básico em funcionamento, é hora de torná-lo mais flexível. Em programação, a flexibilidade é crucial, pois permite que nosso código se adapte a diferentes requisitos. Conseguiremos isso modificando nosso programa `coticker.py` para suportar várias opções de filtragem e formatação.

1. Primeiro, abra o arquivo `coticker.py` em seu editor de código. O editor de código é onde você fará todas as alterações necessárias no programa. Ele fornece um ambiente conveniente para visualizar, editar e salvar seu código.

2. Em seguida, adicionaremos uma nova corrotina que filtra dados por nome da ação. Uma corrotina é um tipo especial de função que pode pausar e retomar sua execução. Isso nos permite criar um pipeline onde os dados podem fluir por diferentes etapas de processamento. Aqui está o código para a nova corrotina:

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

Neste código, a corrotina `filter_by_name` recebe um nome de ação e uma corrotina de destino como parâmetros. Ele espera continuamente por um registro usando a palavra-chave `yield`. Quando um registro chega, ele verifica se o nome do registro corresponde ao nome especificado. Se corresponder, ele envia o registro para a corrotina de destino.

3. Agora, vamos adicionar outra corrotina que filtra com base em limites de preço. Esta corrotina nos ajudará a selecionar ações dentro de uma faixa de preço específica. Aqui está o código:

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

Semelhante à corrotina anterior, a corrotina `price_threshold` espera por um registro. Em seguida, ele verifica se o preço do registro está dentro da faixa de preço mínima e máxima especificada. Se estiver, ele envia o registro para a corrotina de destino.

4. Depois de adicionar as novas corrotinas, precisamos atualizar o programa principal para demonstrar esses filtros adicionais. O programa principal é o ponto de entrada de nossa aplicação, onde configuramos os pipelines de processamento e iniciamos o fluxo de dados. Aqui está o código atualizado:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

Neste código atualizado, criamos três pipelines de processamento diferentes. O primeiro pipeline mostra ações com mudanças negativas, o segundo pipeline filtra ações pelo nome 'AAPL' e o terceiro pipeline filtra ações com base em uma faixa de preço entre 50 e 75. Usamos threads para executar os dois primeiros pipelines simultaneamente, o que nos permite processar dados de forma mais eficiente.

5. Depois de fazer todas as alterações, salve o arquivo. Salvar o arquivo garante que todas as suas modificações sejam preservadas. Em seguida, execute o programa atualizado usando os seguintes comandos em seu terminal:

```bash
cd /home/labex/project
python3 coticker.py
```

O comando `cd` altera o diretório atual para o diretório do projeto, e o comando `python3 coticker.py` executa o programa Python.

6. Após executar o programa, você deverá ver três saídas diferentes:
   - Primeiro, você verá ações com mudanças negativas.
   - Em seguida, você verá todas as atualizações de ações da AAPL.
   - Finalmente, você verá todas as ações com preços entre 50 e 75.

## Entendendo o Pipeline Aprimorado

O programa aprimorado demonstra vários conceitos importantes:

1. **Múltiplos Pipelines**: Podemos criar múltiplos pipelines de processamento a partir da mesma fonte de dados. Isso nos permite realizar diferentes tipos de análise nos mesmos dados simultaneamente.
2. **Filtros Especializados**: Podemos criar diferentes corrotinas para tarefas de filtragem específicas. Esses filtros nos ajudam a selecionar apenas os dados que atendem aos nossos critérios específicos.
3. **Processamento Concorrente**: Usando threads, podemos executar múltiplos pipelines simultaneamente. Isso melhora a eficiência do nosso programa, permitindo que ele processe dados em paralelo.
4. **Composição de Pipeline**: Corrotinas podem ser combinadas de diferentes maneiras para atingir diferentes objetivos de processamento de dados. Isso nos dá a flexibilidade de personalizar nossos pipelines de processamento de dados de acordo com nossas necessidades.

Essa abordagem fornece uma maneira flexível e modular de processar dados de streaming. Ele permite que você adicione ou modifique etapas de processamento sem alterar a arquitetura geral do programa.
