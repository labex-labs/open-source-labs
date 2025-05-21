# Compreendendo a Alocação de Memória de Listas

Em Python, as listas são uma estrutura de dados muito útil, especialmente quando você precisa adicionar elementos a elas. As listas Python são projetadas para serem eficientes para operações de adição (appending). Em vez de alocar exatamente a quantidade de memória necessária, o Python aloca memória extra em antecipação a adições futuras. Essa estratégia minimiza o número de realocações de memória necessárias quando a lista cresce.

Vamos entender melhor esse conceito usando a função `sys.getsizeof()`. Essa função retorna o tamanho de um objeto em bytes, o que nos ajuda a ver quanta memória uma lista está usando em diferentes estágios.

1. Primeiro, você precisa abrir um shell interativo Python no seu terminal. Isso é como um playground onde você pode executar código Python imediatamente. Para abri-lo, digite o seguinte comando no seu terminal e pressione Enter:

```bash
python3
```

2. Depois de entrar no shell interativo Python, você precisa importar o módulo `sys`. Módulos em Python são como caixas de ferramentas que contêm funções úteis. O módulo `sys` tem a função `getsizeof()` que precisamos. Após importar o módulo, crie uma lista vazia chamada `items`. Aqui está o código para fazer isso:

```python
import sys
items = []
```

3. Agora, vamos verificar o tamanho inicial da lista vazia. Usaremos a função `sys.getsizeof()` com a lista `items` como seu argumento. Digite o seguinte código no shell interativo Python e pressione Enter:

```python
sys.getsizeof(items)
```

Você deve ver um valor como `64` bytes. Esse valor representa a sobrecarga (overhead) para uma lista vazia. A sobrecarga é a quantidade básica de memória que o Python usa para gerenciar a lista, mesmo quando ela não tem elementos.

4. Em seguida, começaremos a adicionar itens à lista um por um e observar como a alocação de memória muda. Usaremos o método `append()` para adicionar um elemento à lista e, em seguida, verificar o tamanho novamente. Aqui está o código:

```python
items.append(1)
sys.getsizeof(items)
```

Você deve ver um valor maior, em torno de `96` bytes. Esse aumento no tamanho mostra que o Python alocou mais memória para acomodar o novo elemento.

5. Vamos continuar adicionando mais itens à lista e verificar o tamanho após cada adição. Aqui está o código para fazer isso:

```python
items.append(2)
sys.getsizeof(items)  # Size remains the same

items.append(3)
sys.getsizeof(items)  # Size still unchanged

items.append(4)
sys.getsizeof(items)  # Size still unchanged

items.append(5)
sys.getsizeof(items)  # Size jumps to a larger value
```

Você notará que o tamanho não aumenta com cada operação de adição (append). Em vez disso, ele aumenta periodicamente. Isso demonstra que o Python está alocando memória em blocos (chunks) em vez de individualmente para cada novo item.

Esse comportamento é intencional. O Python aloca mais memória do que o necessário inicialmente para evitar realocações frequentes à medida que a lista cresce. Cada vez que a lista excede sua capacidade atual, o Python aloca um bloco de memória maior.

Lembre-se de que uma lista armazena referências a objetos, não os próprios objetos. Em um sistema de 64 bits, cada referência normalmente requer 8 bytes de memória. Isso é importante para entender porque afeta quanta memória uma lista realmente usa quando contém diferentes tipos de objetos.
