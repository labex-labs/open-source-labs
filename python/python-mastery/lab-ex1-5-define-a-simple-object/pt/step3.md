# Criando Objetos de Ações

Agora que definimos nossa classe `Stock`, é hora de colocá-la em ação. Criar instâncias de uma classe é como fazer exemplos específicos com base em um modelo geral. Neste caso, a classe `Stock` é nosso modelo, e criaremos alguns objetos de ações. Depois de criar esses objetos, aprenderemos como acessar seus atributos (características) e métodos (ações que eles podem realizar).

1. Primeiro, precisamos abrir um terminal no WebIDE. O terminal é como um centro de comando onde podemos dar instruções ao nosso computador. Para abri-lo, clique em "Terminal" no menu.

2. Depois que o terminal estiver aberto, precisamos garantir que estamos no diretório correto do projeto. O diretório do projeto é onde todos os arquivos relevantes para nosso projeto são armazenados. Se você ainda não estiver no diretório do projeto, use o seguinte comando para navegar até lá:

```bash
cd /home/labex/project
```

3. Agora, queremos iniciar o Python no modo interativo com nosso arquivo `stock.py`. O modo interativo nos permite testar nosso código passo a passo e ver os resultados imediatamente. O arquivo `stock.py` contém a definição da nossa classe `Stock`. Use o seguinte comando:

```bash
python3 -i stock.py
```

A flag `-i` é importante aqui. Ela diz ao Python para executar o script `stock.py` primeiro. Após executar o script, ele inicia uma sessão interativa. Nesta sessão, podemos acessar quaisquer classes e variáveis que foram definidas no script `stock.py`.

4. Vamos criar um novo objeto `Stock` para as ações do Google. Criar um objeto é como fazer uma instância específica da classe `Stock` com valores particulares. Use o seguinte código:

```python
s = Stock('GOOG', 100, 490.10)
```

Esta linha de código cria uma nova instância da classe `Stock`. Aqui está o que cada valor significa:

- Name: 'GOOG' - Este é o símbolo das ações do Google.
- Shares: 100 - Representa o número de ações do Google que temos.
- Price: 490.10 - Este é o preço por ação do Google.

5. Agora que temos nosso objeto `Stock`, podemos acessar seus atributos. Atributos são como as propriedades de um objeto. Para acessar um atributo, usamos o nome do objeto seguido por um ponto e o nome do atributo.

```python
s.name
```

Quando você executar este código, ele exibirá o nome da ação:

```
'GOOG'
```

Vamos acessar o número de ações:

```python
s.shares
```

A saída será o número de ações que definimos:

```
100
```

Finalmente, vamos acessar o preço por ação:

```python
s.price
```

A saída será o preço por ação:

```
490.1
```

6. Nossa classe `Stock` tem um método chamado `cost()`. Um método é como uma ação que um objeto pode realizar. Neste caso, o método `cost()` calcula o custo total de nossas ações. Para chamar este método, use o seguinte código:

```python
s.cost()
```

A saída será o custo total:

```
49010.0
```

O método `cost()` funciona multiplicando o número de ações (100) pelo preço por ação (490.10), o que nos dá 49010.0.
