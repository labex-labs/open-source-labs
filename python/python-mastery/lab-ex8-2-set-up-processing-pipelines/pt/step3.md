# Construindo um Pipeline de Dados Mais Complexo

Agora, vamos levar nosso pipeline de dados para o próximo nível, adicionando filtragem e melhorando a apresentação dos dados. Isso tornará mais fácil analisar e entender as informações com as quais estamos trabalhando. Faremos alterações em nosso script `ticker.py`. A filtragem dos dados nos ajudará a nos concentrar nas informações específicas que nos interessam, e apresentá-los em uma tabela bem formatada tornará mais legível.

## Atualizando o Arquivo ticker.py

1. Primeiro, abra seu arquivo `ticker.py` no WebIDE. O WebIDE é uma ferramenta que permite escrever e editar código diretamente em seu navegador. Ele fornece um ambiente conveniente para fazer alterações em seus scripts Python.

2. Em seguida, precisamos substituir o bloco `if __name__ == '__main__':` no arquivo `ticker.py` pelo seguinte código. Este bloco de código é o ponto de entrada do nosso script, e ao substituí-lo, estaremos alterando como o script processa e exibe os dados.

```python
if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
```

3. Depois de fazer essas alterações, salve o arquivo. Você pode fazer isso pressionando `Ctrl+S` no teclado ou selecionando "File" → "Save" no menu. Salvar o arquivo garante que suas alterações sejam preservadas e possam ser executadas posteriormente.

## Entendendo o Pipeline Aprimorado

Vamos dar uma olhada mais de perto no que este pipeline aprimorado faz. Entender cada etapa o ajudará a ver como as diferentes partes do código trabalham juntas para processar e exibir os dados.

1. Começamos importando `create_formatter` e `print_table` do módulo `tableformat`. Este módulo já está configurado para você, e ele fornece funções que nos ajudam a formatar e imprimir os dados em uma tabela agradável.

2. Em seguida, criamos um formatador de texto usando `create_formatter('text')`. Este formatador será usado para formatar os dados de uma forma que seja fácil de ler.

3. Agora, vamos detalhar o pipeline passo a passo:
   - `follow('stocklog.csv')` é uma função que gera linhas do arquivo `stocklog.csv`. Ele monitora continuamente o arquivo em busca de novos dados e fornece as linhas uma por uma.
   - `csv.reader(lines)` pega as linhas geradas por `follow` e as analisa em dados de linha. Isso é necessário porque os dados no arquivo CSV estão em um formato de texto, e precisamos convertê-los em um formato estruturado com o qual possamos trabalhar.
   - `(Ticker.from_row(row) for row in rows)` é uma expressão geradora que converte cada linha de dados em um objeto `Ticker`. Um objeto `Ticker` representa uma ação e contém informações como o nome, preço e mudança da ação.
   - `(rec for rec in records if rec.change < 0)` é outra expressão geradora que filtra os objetos `Ticker`. Ele mantém apenas os objetos onde a mudança de preço da ação é negativa. Isso nos permite focar nas ações que diminuíram de preço.
   - `print_table(negative, ['name', 'price', 'change'], formatter)` pega os objetos `Ticker` filtrados e os formata em uma tabela usando o formatador que criamos anteriormente. Em seguida, ele imprime a tabela no console.

Este pipeline demonstra o poder dos geradores. Em vez de carregar todos os dados do arquivo na memória de uma vez, estamos encadeando várias operações (leitura, análise, conversão, filtragem) e processando os dados um item por vez. Isso economiza memória e torna o código mais eficiente.

## Executando o Pipeline Aprimorado

Vamos executar o código atualizado para ver os resultados.

1. Primeiro, certifique-se de estar no diretório do projeto no terminal. Se você ainda não estiver lá, pode navegar até ele usando o seguinte comando:

   ```bash
   cd /home/labex/project
   ```

2. Depois de estar no diretório do projeto, execute o script `ticker.py` usando o seguinte comando:

   ```bash
   python3 ticker.py
   ```

3. Após executar o script, você deve ver uma tabela bem formatada no terminal. Esta tabela mostra apenas as ações com mudanças de preço negativas.

   ```
          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19
   ```

Se você viu saída suficiente e deseja interromper a execução do script, pode pressionar `Ctrl+C` no teclado.

## O Poder dos Pipelines de Geradores

O que criamos aqui é um poderoso pipeline de processamento de dados. Vamos resumir o que ele faz:

1. Ele monitora continuamente o arquivo `stocklog.csv` em busca de novos dados. Isso significa que, à medida que novos dados são adicionados ao arquivo, o pipeline os processará automaticamente.
2. Ele analisa os dados CSV do arquivo em objetos `Ticker` estruturados. Isso torna mais fácil trabalhar com os dados e realizar operações neles.
3. Ele filtra os dados com base em um critério específico, neste caso, mudanças de preço negativas. Isso nos permite focar nas ações que estão perdendo valor.
4. Ele formata e apresenta os dados filtrados em uma tabela legível. Isso facilita a análise dos dados e a conclusão de conclusões.

Uma das principais vantagens de usar geradores neste pipeline é que ele usa memória mínima. Os geradores produzem valores sob demanda, o que significa que eles não armazenam todos os dados na memória de uma vez. Isso é semelhante aos pipes Unix, onde cada componente processa os dados e os passa para o próximo componente.

Você pode pensar nos geradores como blocos de Lego. Assim como você pode empilhar blocos de Lego para criar estruturas diferentes, você pode combinar geradores para criar fluxos de trabalho de processamento de dados poderosos. Essa abordagem modular permite que você construa sistemas complexos a partir de componentes simples e reutilizáveis.
