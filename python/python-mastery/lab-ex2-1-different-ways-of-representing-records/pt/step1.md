# Explorando o Conjunto de Dados

Vamos começar nossa jornada dando uma olhada de perto no conjunto de dados com o qual vamos trabalhar. O arquivo `ctabus.csv` é um arquivo CSV (Comma-Separated Values - Valores Separados por Vírgula). Arquivos CSV são uma forma comum de armazenar dados tabulares, onde cada linha representa uma linha e os valores dentro de uma linha são separados por vírgulas. Este arquivo em particular contém dados diários de passageiros para o sistema de ônibus da Chicago Transit Authority (CTA), cobrindo o período de 1º de janeiro de 2001 a 31 de agosto de 2013.

Descompacte o arquivo e remova o arquivo zip:

```bash
cd /home/labex/project
unzip ctabus.csv.zip
rm ctabus.csv.zip
```

Para entender a estrutura deste arquivo, primeiro vamos dar uma olhada nele. Usaremos Python para ler o arquivo e imprimir algumas linhas. Abra um terminal e execute o seguinte código Python:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

Neste código, primeiro abrimos o arquivo usando a função `open` e o atribuímos à variável `f`. A função `next` é usada para ler a próxima linha do arquivo. Usamos isso três vezes: a primeira vez para ler a linha do cabeçalho, que geralmente contém os nomes das colunas no conjunto de dados. A segunda e terceira vezes, lemos a primeira e a segunda linhas de dados, respectivamente. Finalmente, fechamos o arquivo usando o método `close` para liberar recursos do sistema.

Você deve ver uma saída semelhante a esta:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Esta saída mostra que o arquivo tem 4 colunas de dados. Vamos detalhar o que cada coluna representa:

1.  `route`: Este é o nome ou número da rota do ônibus. É a primeira coluna (Coluna 0) no conjunto de dados.
2.  `date`: É uma string de data no formato MM/DD/YYYY. Esta é a segunda coluna (Coluna 1).
3.  `daytype`: É um código de tipo de dia, que é a terceira coluna (Coluna 2).
    - U = Domingo/Feriado
    - A = Sábado
    - W = Dia de semana
4.  `rides`: Esta coluna registra o número total de passageiros como um inteiro. É a quarta coluna (Coluna 3).

A coluna `rides` nos diz quantas pessoas embarcaram em um ônibus em uma rota específica em um determinado dia. Por exemplo, na saída acima, podemos ver que 7.354 pessoas andaram no ônibus número 3 em 1º de janeiro de 2001.

Agora, vamos descobrir quantas linhas existem no arquivo. Saber o número de linhas nos dará uma ideia do tamanho do nosso conjunto de dados. Execute o seguinte código Python:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

Neste código, usamos a instrução `with` para abrir o arquivo. A vantagem de usar `with` é que ele cuida automaticamente de fechar o arquivo quando terminamos com ele. Em seguida, usamos uma expressão geradora `(1 for line in f)` para criar uma sequência de 1s, um para cada linha no arquivo. A função `sum` soma todos esses 1s, dando-nos o número total de linhas no arquivo. Finalmente, imprimimos o resultado.

Isso deve gerar aproximadamente 577.564 linhas, o que significa que estamos lidando com um conjunto de dados substancial. Este grande conjunto de dados nos fornecerá muitos dados para analisar e obter insights.
