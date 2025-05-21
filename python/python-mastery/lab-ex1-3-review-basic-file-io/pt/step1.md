# Compreendendo o Problema

Nesta etapa, primeiro entenderemos qual é o problema que precisamos resolver e, em seguida, daremos uma olhada nos dados com os quais trabalharemos. Esta é uma primeira etapa importante em qualquer tarefa de programação, pois nos ajuda a saber exatamente o que estamos almejando e quais recursos temos à nossa disposição.

No seu diretório do projeto, há um arquivo chamado `portfolio.dat`. Este arquivo armazena informações sobre um portfólio de ações. Um portfólio é como uma coleção de diferentes ações que um investidor possui. Cada linha neste arquivo representa uma única compra de ação. O formato de cada linha é o seguinte:

```
[Símbolo da Ação] [Número de Ações] [Preço por Ação]
```

O símbolo da ação é um código curto que representa a ação de uma empresa específica. O número de ações nos diz quantas unidades daquela ação foram compradas, e o preço por ação é o custo de uma unidade daquela ação.

Vamos dar uma olhada em um exemplo. Considere a primeira linha do arquivo:

```
AA 100 32.20
```

Esta linha indica que 100 ações da ação com o símbolo "AA" foram compradas. Cada ação custou $32.20.

Se você quiser ver o que está dentro do arquivo `portfolio.dat`, você pode executar o seguinte comando no terminal. O comando `cat` é uma ferramenta útil no terminal que permite visualizar o conteúdo de um arquivo.

```bash
cat ~/project/portfolio.dat
```

Agora, sua tarefa é criar um programa Python chamado `pcost.py`. Este programa executará três tarefas principais:

1. Primeiro, ele precisa abrir e ler o arquivo `portfolio.dat`. Abrir um arquivo em Python permite que nosso programa acesse os dados armazenados nele.
2. Em seguida, ele precisa calcular o custo total de todas as compras de ações no portfólio. Para fazer isso, para cada linha no arquivo, precisamos multiplicar o número de ações pelo preço por ação. Depois de obter esses valores para cada linha, somamos todos eles. Isso nos dá o valor total de dinheiro gasto em todas as ações do portfólio.
3. Finalmente, o programa deve gerar o custo total. Desta forma, podemos ver o resultado de nossos cálculos.

Vamos começar criando o arquivo `pcost.py`. Você pode usar o editor para abrir e editar este arquivo. Ele já foi criado para você durante a etapa de configuração. Este arquivo será o local onde você escreverá o código Python para resolver o problema que acabamos de discutir.
