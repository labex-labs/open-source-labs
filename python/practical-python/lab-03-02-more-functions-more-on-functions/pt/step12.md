# Reatribuição (Reassignment) vs. Modificação (Modifying)

Certifique-se de entender a sutil diferença entre modificar um valor e reatribuir um nome de variável.

```python
def foo(items):
    items.append(42)    # Modifica o objeto de entrada

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Altera a variável local `items` para apontar para um objeto diferente

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

_Lembrete: A atribuição de variáveis nunca sobrescreve a memória. O nome é meramente vinculado a um novo valor._

Este conjunto de exercícios fará com que você implemente o que é, talvez, a parte mais poderosa e difícil do curso. Há muitos passos e muitos conceitos de exercícios anteriores são reunidos de uma só vez. A solução final tem apenas cerca de 25 linhas de código, mas reserve um tempo e certifique-se de entender cada parte.

Uma parte central do seu programa `report.py` se concentra na leitura de arquivos CSV. Por exemplo, a função `read_portfolio()` lê um arquivo contendo linhas de dados de portfólio e a função `read_prices()` lê um arquivo contendo linhas de dados de preços. Em ambas as funções, há muitos detalhes de baixo nível e recursos semelhantes. Por exemplo, ambas abrem um arquivo e o envolvem com o módulo `csv` e ambas convertem vários campos em novos tipos.

Se você estivesse fazendo muita análise de arquivos na vida real, provavelmente gostaria de limpar um pouco disso e torná-lo mais genérico. Esse é o nosso objetivo.

Comece este exercício abrindo o arquivo chamado `fileparse.py`. É aqui que faremos nosso trabalho.
