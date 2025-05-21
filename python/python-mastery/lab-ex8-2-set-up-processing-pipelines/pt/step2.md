# Criando a Classe Ticker

No processamento de dados, trabalhar com dados brutos pode ser bastante desafiador. Para tornar nosso trabalho com dados de ações mais organizado e eficiente, definiremos uma classe adequada para representar as cotações de ações. Essa classe servirá como um modelo para nossos dados de ações, tornando nosso pipeline de processamento de dados mais robusto e fácil de gerenciar.

## Criando o Arquivo ticker.py

1. Primeiro, precisamos criar um novo arquivo no WebIDE. Você pode fazer isso clicando no ícone "New File" ou clicando com o botão direito no explorador de arquivos e selecionando "New File". Nomeie este arquivo `ticker.py`. Este arquivo conterá o código para nossa classe `Ticker`.

2. Agora, vamos adicionar o seguinte código ao seu arquivo `ticker.py` recém-criado. Este código definirá nossa classe `Ticker` e configurará um pipeline de processamento simples para testá-la.

```python
# ticker.py

from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. Após adicionar o código, salve o arquivo. Você pode fazer isso pressionando `Ctrl+S` ou selecionando "File" → "Save" no menu. Salvar o arquivo garante que suas alterações sejam preservadas e possam ser executadas posteriormente.

## Entendendo o Código

Vamos dar uma olhada mais de perto no que este código faz passo a passo:

1. No início do código, estamos importando `Structure` e tipos de campo do módulo `structure.py`. Este módulo já foi configurado para você. Essas importações são essenciais porque fornecem os blocos de construção para nossa classe `Ticker`. A classe `Structure` será a classe base para nossa classe `Ticker`, e os tipos de campo como `String`, `Float` e `Integer` definirão os tipos de dados de nossos campos de dados de ações.

2. Em seguida, definimos uma classe `Ticker` que herda de `Structure`. Esta classe tem vários campos que representam diferentes aspectos dos dados das ações:

   - `name`: Este campo armazena o símbolo da ação, como "IBM" ou "AAPL". Ele nos ajuda a identificar com qual ação da empresa estamos lidando.
   - `price`: Ele contém o preço atual da ação. Esta é uma informação crucial para os investidores.
   - `date` e `time`: Esses campos nos dizem quando a cotação da ação foi gerada. Saber a hora e a data é importante para analisar as tendências de preços das ações ao longo do tempo.
   - `change`: Isso representa a mudança de preço da ação. Ele mostra se o preço da ação subiu ou desceu em comparação com um ponto anterior.
   - `open`, `high`, `low`: Esses campos representam o preço de abertura, o preço mais alto e o preço mais baixo da ação durante um determinado período. Eles nos dão uma ideia da faixa de preço da ação.
   - `volume`: Este campo armazena o número de ações negociadas. Um alto volume de negociação pode indicar um forte interesse do mercado em uma ação específica.

3. No bloco `if __name__ == '__main__':`, configuramos um pipeline de processamento. Este bloco de código será executado quando executarmos o arquivo `ticker.py` diretamente.
   - `follow('stocklog.csv')` é uma função que gera linhas do arquivo `stocklog.csv`. Ele nos permite ler o arquivo linha por linha.
   - `csv.reader(lines)` pega essas linhas e as analisa em dados de linha. CSV (Valores Separados por Vírgula) é um formato de arquivo comum para armazenar dados tabulares, e esta função nos ajuda a extrair os dados de cada linha.
   - `(Ticker.from_row(row) for row in rows)` é uma expressão geradora. Ele pega cada linha de dados e a converte em um objeto `Ticker`. Dessa forma, transformamos os dados CSV brutos em objetos estruturados que são mais fáceis de trabalhar.
   - O loop `for` itera sobre esses objetos `Ticker` e imprime cada um. Isso nos permite ver os dados estruturados em ação.

## Executando o Código

Vamos executar o código para ver como ele funciona:

1. Primeiro, precisamos ter certeza de que estamos no diretório do projeto no terminal. Se você ainda não estiver lá, use o seguinte comando para navegar até ele:

   ```bash
   cd /home/labex/project
   ```

2. Depois de estar no diretório correto, execute o script `ticker.py` usando o seguinte comando:

   ```bash
   python3 ticker.py
   ```

3. Após executar o script, você deve ver uma saída semelhante a esta (seus dados variarão):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

Você pode parar a execução do script pressionando `Ctrl+C` quando tiver visto saída suficiente.

Observe como os dados CSV brutos foram transformados em objetos `Ticker` estruturados. Essa transformação torna os dados muito mais fáceis de trabalhar em nosso pipeline de processamento, pois agora podemos acessar e manipular os dados das ações usando os campos definidos na classe `Ticker`.
